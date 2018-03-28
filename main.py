import eyetrack_aoi_task_count_bar
import eyetrack_spatial_participants as et_part
import eyetrack_aoi_task_count as et_aoi_task_count
import eyetrack_spatial_error_time as et_spat_err
import eyetrack_aoi_participant_count
import eyetrack_aoi_histogram
import eyetrack_pupil_dilation
import response_times_condition_boxplot as response_times

# TODO you can also change the output to PDF or SVG!

#eyetrack_pupil_dilation.draw_timeline_over_time_all_participants('pupil_dilation_time_sec.csv', 'eyetrack_pupil_dilation_time_sec.png')
eyetrack_pupil_dilation.draw_timeline_per_conditions('pupil_dilation_condition.csv', 'eyetrack_pupil_dilation_condition.png')

if False:
    # AOI Analysis
    et_aoi_task_count.draw_plot('aoi_task_comprehension_time_count.csv', 'eyetrack_aoi_task_python_count.png')
    eyetrack_aoi_task_count_bar.draw_plot('aoi_task_comprehension_count_bar.csv', 'eyetrack_aoi_task_python_count_bar.png')
    eyetrack_aoi_participant_count.draw_plot('aoi_task_participant_count.csv', 'eyetrack_aoi_participant_python_count.png')

    eyetrack_aoi_histogram.draw_plot('aoi_histogram_count.csv', 'eyetrack_aoi_histogram_count.png')
    eyetrack_aoi_histogram.draw_plot('aoi_histogram_time.csv', 'eyetrack_aoi_histogram_time.png')

    # Response Time
    response_times.draw_response_times_plot('ResponseTimeExport.csv', 'response_times.png')

    # Ogama
    et_spat_err.draw_eyetrack_spatial_error_plot('EyetrackSpatialErrorExport.csv', 'eyetrack_spatial_error_condition_ogama_raw.png')
    et_spat_err.draw_eyetrack_spatial_error_plot('EyetrackSpatialErrorExportWeighted.csv', 'eyetrack_spatial_error_condition_ogama_weighted.png')

    et_part.draw_eyetrack_spatial_error_plot('FixationRestAnalysisPartV2.csv', 'eyetrack_spatial_error_participants_ogama_weighted.png')

    et_part.draw_eyetrack_spatial_error_plot('FixationRestAnalysisPartV2.csv', 'eyetrack_spatial_error_participants_ogama_weighted_indiv_x.png', True, False, 'x')
    et_part.draw_eyetrack_spatial_error_plot('FixationRestAnalysisPartV2.csv', 'eyetrack_spatial_error_participants_ogama_weighted_indiv_y.png', True, False, 'y')

    # Python
    et_spat_err.draw_eyetrack_spatial_error_plot('average_offset_participant.csv', 'eyetrack_spatial_error_condition_python_raw.png')
    et_spat_err.draw_eyetrack_spatial_error_plot('average_offset_participant_weighted.csv', 'eyetrack_spatial_error_condition_python_weighted.png')

    et_part.draw_eyetrack_spatial_error_plot('average_offset_participant.csv', 'eyetrack_spatial_error_participants_python_raw.png')
    et_part.draw_eyetrack_spatial_error_plot('average_offset_participant.csv', 'eyetrack_spatial_error_participants_python_raw_indiv_x.png', True, False, 'x')
    et_part.draw_eyetrack_spatial_error_plot('average_offset_participant.csv', 'eyetrack_spatial_error_participants_python_raw_indiv_y.png', True, False, 'y')

    et_part.draw_eyetrack_spatial_error_plot('average_offset_participant_weighted.csv', 'eyetrack_spatial_error_participants_python_weighted.png')
    et_part.draw_eyetrack_spatial_error_plot('average_offset_participant_weighted.csv', 'eyetrack_spatial_error_participants_python_weighted_indiv_x.png', True, False, 'x')
    et_part.draw_eyetrack_spatial_error_plot('average_offset_participant_weighted.csv', 'eyetrack_spatial_error_participants_python_weighted_indiv_y.png', True, False, 'y')
