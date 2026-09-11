SDACS Amy MATLAB Handoff
Generated from: Amy_MATLAB_4_Node_Data_Dump.zip

Purpose
-------
This folder gives Amy a clean starting point for MATLAB room-map plots. Use the summary files first, not the full raw per-second dataset.

Main file to use first
----------------------
amy_matlab_roommap_summary_best_runs.csv

This file has one recommended 4-node summary set per label where possible. It includes x_m, y_m, z_metric, and z_value so Amy can make a quick scatter3 plot:

    x = x_m
    y = y_m
    z = z_value
    color/grouping = label or dominant_band_mode

Important files
---------------
1. amy_matlab_roommap_summary_best_runs.csv
   Best capture summaries for MATLAB plotting. This is the easiest starting file.

2. amy_node_positions_template.csv
   Placeholder node coordinates. Update x_m/y_m/height_m to the real room layout before final plots.

3. amy_matlab_summary_corrected_all_runs.csv
   Full corrected summary table. 15 kHz target frequency metadata has been corrected from 5000 to 15000.

4. amy_matlab_column_dictionary.csv
   Column meanings for the summary file.

Recommended MATLAB workflow
---------------------------
1. Import amy_matlab_roommap_summary_best_runs.csv.
2. Confirm rows, labels, and nodes.
3. Keep amy_node_positions_template.csv the same based on synthetic locations.
4. Join by node_id if you want to replace the placeholder coordinates.
5. Plot x_m, y_m, z_value for each label.
6. Repeat plots using z_metric / z_value or specific mean band ratio columns.

Suggested z-axis by label (Ignore this if you already have you're own method)
-------------------------
- test_tone_100hz: mean_band_bass_ratio
- test_tone_500hz: mean_band_low_mid_ratio
- test_tone_2khz: mean_band_mid_ratio
- test_tone_5khz: mean_band_presence_ratio or mean_band_high_ratio
- test_tone_15khz: mean_band_high_ratio

Known notes
-----------
- SPL/db_spl is not calibrated yet. Treat it as a reference only.
- Band ratios are better for the first MATLAB plots.
- The 15 kHz target frequency metadata was wrong in the original exported files and has been corrected here.
- The summary file had a complete 15 kHz run that was not present in the raw acoustic feature CSV. The column raw_rows_available_in_sdacs_acoustic_features_csv shows this.
- About 59 rows means a healthy 60 s capture, since the firmware publishes about once per second.

Quick MATLAB starter
--------------------
T = readtable("amy_matlab_roommap_summary_best_runs.csv", "TextType", "string");
figure;
scatter3(T.x_m, T.y_m, T.z_value, 80, T.z_value, "filled");
grid on;
xlabel("Room X (m)"); ylabel("Room Y (m)"); zlabel("Selected feature ratio");
title("SDACS 4-Node Acoustic Room Map");
colorbar;
text(T.x_m, T.y_m, T.z_value, T.node_id);
