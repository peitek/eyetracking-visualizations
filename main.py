import eyetrack_aoi_task_count_bar
import eyetrack_spatial_participants as et_part
import eyetrack_spatial_error_time as et_spat_err
import eyetrack_aoi_participant_count
import eyetrack_aoi_histogram
import eyetrack_pupil_dilation
import eyetrack_blink_rates

# TODO think about changing the output to PDF or SVG!
# TODO think of automatically creating all charts for all participants

if True:
    # Pupil dilation per condition/snippet
    eyetrack_pupil_dilation.draw_timeline_per_conditions('pupil_dilation_condition.csv', 'eyetrack_pupil_dilation_condition_filtered', True)
    eyetrack_pupil_dilation.draw_timeline_per_conditions('pupil_dilation_condition.csv', 'eyetrack_pupil_dilation_condition', False)
    eyetrack_pupil_dilation.draw_timeline_per_conditions('pupil_dilation_condition.csv', 'eyetrack_pupil_dilation_condition', False, "p01")

    eyetrack_pupil_dilation.draw_timeline_per_snippet('pupil_dilation_snippet.csv', 'eyetrack_pupil_dilation_snippet', 'Compr_BU')
    eyetrack_pupil_dilation.draw_timeline_per_snippet('pupil_dilation_snippet.csv', 'eyetrack_pupil_dilation_snippet', 'Compr_TD_B')
    eyetrack_pupil_dilation.draw_timeline_per_snippet('pupil_dilation_snippet.csv', 'eyetrack_pupil_dilation_snippet', 'Compr_TD_N')

    eyetrack_pupil_dilation.draw_timeline_per_snippet_brightness('pupil_dilation_snippet.csv', 'eyetrack_pupil_dilation_snippet_brightness_complete', False)
    eyetrack_pupil_dilation.draw_timeline_per_snippet_brightness('pupil_dilation_snippet.csv', 'eyetrack_pupil_dilation_snippet_brightness_compr', True)

    eyetrack_pupil_dilation.analyze_pupil_dilation_per_condition('pupil_dilation_snippet_participant.csv')
    eyetrack_pupil_dilation.analyze_pupil_dilation_per_condition('pupil_dilation_snippet_participant.csv', True, True)
    eyetrack_pupil_dilation.normalize_analyze_pupil_dilation_per_condition('pupil_dilation_snippet_participant.csv')

    eyetrack_pupil_dilation.analyze_pupil_dilation_per_snippet('pupil_dilation_snippet_participant.csv')

    # Pupil dilation timelines
    eyetrack_pupil_dilation.draw_timeline_over_time_all_participants('pupil_dilation_time_sec.csv', 'eyetrack_pupil_dilation_time_sec.png')

    eyetrack_pupil_dilation.draw_timeline_per_snippet_brightness('pupil_dilation_snippet_participant.csv', 'eyetrack_pupil_dilation_snippet_brightness_compr_sum', True, True)

    eyetrack_pupil_dilation.draw_timeline_per_snippet_compare('pupil_dilation_snippet.csv', 'eyetrack_pupil_dilation_snippet_compare_arrayavg', 'arrayAverageTD_B.png', 'beebtBurebzrTD_N.png')
    eyetrack_pupil_dilation.draw_timeline_per_snippet_compare('pupil_dilation_snippet.csv', 'eyetrack_pupil_dilation_snippet_compare_power', 'powerTD_B.png', 'buycpTD_N.png')
    eyetrack_pupil_dilation.draw_timeline_per_snippet_compare('pupil_dilation_snippet.csv', 'eyetrack_pupil_dilation_snippet_compare_substring', 'containsSubstringTD_B.png', 'ecnzaqnkKopkzvqnmTD_N.png')
    eyetrack_pupil_dilation.draw_timeline_per_snippet_compare('pupil_dilation_snippet.csv', 'eyetrack_pupil_dilation_snippet_compare_commonchrs', 'countSameCharsAtSamePositionTD_B.png', 'ecoamKayiEoaikAmKayiEckqmqcaTD_N.png')
    eyetrack_pupil_dilation.draw_timeline_per_snippet_compare('pupil_dilation_snippet.csv', 'eyetrack_pupil_dilation_snippet_compare_threshold', 'firstAboveTresholdTD_B.png', 'vsjihAzmfwHjwitmpxTD_N.png')

    eyetrack_pupil_dilation.draw_timeline_over_time_all_participants('pupil_dilation_gaze_pos_time_sec.csv', 'eyetrack_pupil_dilation_time_sec', True, "p01")

    eyetrack_pupil_dilation.draw_timeline_over_time_all_participants('pupil_dilation_gaze_pos_time_sec.csv', 'eyetrack_pupil_dilation_time_sec', True, "p01", True)

    eyetrack_pupil_dilation.draw_corrected_timeline_over_time_all_participants('pupil_dilation_gaze_pos_time_sec.csv', 'eyetrack_pupil_dilation_time_sec', True, "p01", True)

    # Blink rates
    eyetrack_blink_rates.analyze_blink_rates_per_snippet('blink_rate_snippet_participant.csv')
    eyetrack_blink_rates.analyze_blink_duration_per_condition('blink_rate_snippet_participant.csv')
    eyetrack_blink_rates.analyze_blink_duration_per_snippet('blink_rate_snippet_participant.csv')

    # AOI Analysis
    eyetrack_aoi_task_count_bar.draw_plot('aoi_task_comprehension_count_bar.csv', 'eyetrack_aoi_task_python_count_bar.png')
    eyetrack_aoi_participant_count.draw_plot('aoi_task_participant_count.csv', 'eyetrack_aoi_participant_python_count.png')

    eyetrack_aoi_histogram.draw_plot('aoi_histogram_count.csv', 'eyetrack_aoi_histogram_count.png')
    eyetrack_aoi_histogram.draw_plot('aoi_histogram_time.csv', 'eyetrack_aoi_histogram_time.png')

    # Fixation analysis based on Python data
    et_spat_err.draw_eyetrack_spatial_error_plot('average_offset_participant.csv', 'eyetrack_spatial_error_condition_python_raw.png')
    et_spat_err.draw_eyetrack_spatial_error_plot('average_offset_participant_weighted.csv', 'eyetrack_spatial_error_condition_python_weighted.png')

    et_part.draw_eyetrack_spatial_error_plot('average_offset_participant_weighted.csv', 'eyetrack_spatial_error_participants_python_weighted.png')
    et_part.draw_eyetrack_spatial_error_plot('average_offset_participant_weighted.csv', 'eyetrack_spatial_error_participants_python_weighted_indiv_x.png', True, False, 'x')
    et_part.draw_eyetrack_spatial_error_plot('average_offset_participant_weighted.csv', 'eyetrack_spatial_error_participants_python_weighted_indiv_y.png', True, False, 'y')

    # Response Time (TODO not eye-tracking related, move to other project)
    # response_times.draw_response_times_plot('ResponseTimeExport.csv', 'response_times.png')

    # Fixation analysis based on Ogama data (TODO this seems currently broken)
    # et_spat_err.draw_eyetrack_spatial_error_plot('EyetrackSpatialErrorExport.csv', 'eyetrack_spatial_error_condition_ogama_raw.png')
    # et_spat_err.draw_eyetrack_spatial_error_plot('EyetrackSpatialErrorExportWeighted.csv', 'eyetrack_spatial_error_condition_ogama_weighted.png')

    # et_part.draw_eyetrack_spatial_error_plot('FixationRestAnalysisPartV2.csv', 'eyetrack_spatial_error_participants_ogama_weighted.png')

    # et_part.draw_eyetrack_spatial_error_plot('FixationRestAnalysisPartV2.csv', 'eyetrack_spatial_error_participants_ogama_weighted_indiv_x.png', True, False, 'x')
    # et_part.draw_eyetrack_spatial_error_plot('FixationRestAnalysisPartV2.csv', 'eyetrack_spatial_error_participants_ogama_weighted_indiv_y.png', True, False, 'y')

