# SDACS Dataset Cleaning, Quality Review, and Capstone Completion Plan

## Final cleaned dataset

- Raw input rows: **11,426**
- Final node-level rows: **11,040**
- Final room-fused rows: **2,760**
- Logical captures: **24** (4 per label)
- Nodes: **4**
- Labels: **6**
- Node-level balance: **1,840 rows per label**
- Room-fused balance: **460 rows per label**
- Training/testing split: **75% / 25% by complete capture**

## What was cleaned

1. Combined the two corrected CSV exports.
2. Preserved the backend-compatible class ID `quiet_room_white_noise`.
3. Split the four-minute quiet-room run into two logical two-minute captures.
4. Removed two unmatched tail rows so all four nodes align.
5. Removed the first and last two seconds of every logical capture.
6. Verified sample-rate status, calibration flags, finite numeric data, ratio bounds, and sensor ranges.
7. Removed label-leakage fields such as `target_band` and `suggested_z_metric`.
8. Removed constants, calibration-only features, environmental/time fields, and deterministic duplicates.
9. Created a capture-grouped train/test split.
10. Created a room-fused dataset using across-node mean, standard deviation, and range.

## Offline quality sanity check

These figures are from a local Random Forest used only to audit generalization. They are not Edge Impulse model results.

- Node-level, unseen-capture accuracy: **23.8%**
- Room-fused, unseen-capture accuracy: **47.2%**
- Six-class chance accuracy: **16.7%**

Room-fused per-class recall:
- `low`: **62.6%**
- `speech`: **17.4%**
- `mid`: **60.0%**
- `high`: **16.5%**
- `noisy`: **49.6%**
- `quiet_room_white_noise`: **77.4%**

Cross-node transfer accuracy, where one complete node was excluded from training:
- `node01` held out: **15.9%**
- `node02` held out: **16.4%**
- `node03` held out: **17.0%**
- `node04` held out: **17.0%**

## Interpretation

- The data is structurally clean and perfectly balanced.
- The current one-second firmware features overlap heavily across the six classes.
- Room fusion improves the result because SDACS is a distributed four-node system.
- The poor cross-node scores indicate meaningful microphone/node response differences.
- `speech` and `mid` are physically overlapping concepts; `noisy` can also contain low, mid, and high energy. A single mutually exclusive six-class target is therefore intrinsically difficult.

## Highest-priority data-quality improvements

1. **Calibrate every node.** Use the same reference speaker, position, 1 kHz tone, and pink-noise sweep. Store per-node level and band-response corrections.
2. **Randomize capture order.** The present session collected labels in blocks. Future sessions should interleave labels so time, temperature, and humidity cannot act as proxies.
3. **Add source metadata.** Record `source_clip_id`, speaker/instrument, playback level, speaker position, room, day, and operator.
4. **Increase source diversity.** Use at least 8-12 distinct sources per label, multiple playback levels, and multiple positions.
5. **Separate scene and spectrum tasks.** A stronger design is:
   - Scene classifier: quiet room / speech / noisy
   - Spectral classifier: low-dominant / mid-dominant / high-dominant
6. **Capture raw PCM where practical.** One-second spectral summaries discard temporal patterns that distinguish speech, cymbals, café noise, and instruments. Edge Impulse MFE or spectrogram features from raw audio should improve these classes.
7. **Keep capture-level holdouts.** Never split individual seconds from the same source capture across training and testing.

## Practical capstone completion path

### 1. Freeze and document the data pipeline
- ESP32-S3 nodes produce acoustic telemetry.
- MQTT and Node-RED perform synchronized labelled capture.
- Raspberry Pi stores the CSV and exposes backend services.
- The cleaning audit and feature dictionary become controlled project artifacts.

### 2. Train the Edge Impulse proof-of-concept
- Use the room-fused training/testing CSVs first.
- Keep `capture_id` as grouping metadata.
- Record the confusion matrix, per-class metrics, model size, and inference latency.
- Treat the first model as an engineering result, even if accuracy remains moderate; explain the class overlap and node-calibration findings.

### 3. Deploy the model on the Raspberry Pi
- Export the trained impulse as a Linux `.eim` model.
- Run inference in the Raspberry Pi backend rather than separately on all four ESP32 nodes.
- Aggregate probabilities over a completed capture and return one stable room classification.

Suggested backend response:

```json
{
  "run_id": "capture_...",
  "classification": "quiet_room_white_noise",
  "confidence": 0.74,
  "probabilities": {
    "low": 0.05,
    "speech": 0.06,
    "mid": 0.04,
    "high": 0.03,
    "noisy": 0.08,
    "quiet_room_white_noise": 0.74
  },
  "model_version": "sdacs-ei-v1",
  "rows_used": 115
}
```

### 4. Complete the Flutter AI screen
- Latest room classification
- Confidence and per-class probability bars
- Capture timestamp and model version
- Suggested issue, such as low-frequency buildup or excessive room noise
- Link to the acoustic map or node comparison

### 5. Use MATLAB as analysis evidence, not a runtime dependency
- Plot feature distributions by label and node.
- Create PCA or cluster plots to show class overlap.
- Produce the 3D low/mid/high room visualization.
- Export figures or JSON/PNG results that the backend can serve.

### 6. Final verification and demonstration
- Demonstrate Node-RED starting a labelled capture.
- Confirm all four nodes contribute complete rows.
- Show the backend reading the latest completed capture.
- Show the Edge Impulse classification response.
- Show the same result in Flutter.
- Compare backend JSON with the Flutter display.
- Record latency from capture completion to GUI update.

### 7. Final-report evidence
- System block diagram and end-to-end data-flow diagram
- Node-RED capture UI and CSV schema
- Cleaning audit and label-balance table
- Edge Impulse data explorer, confusion matrix, and deployment profile
- MATLAB room maps and feature-separation figures
- Backend JSON and matching Flutter screenshots
- Test results, limitations, risk controls, and next iteration

## Definition of a defensible final result

The project does not need to claim that the six-class model is production-ready. A strong final result is a working distributed acoustic sensing pipeline, a documented and repeatable dataset process, an honestly evaluated Edge Impulse model, Raspberry Pi inference, and a Flutter visualization that closes the loop from capture to decision.