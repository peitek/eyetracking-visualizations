import eyetrack_aoi_task_count_bar
import eyetrack_spatial_participants as et_part
import eyetrack_aoi_task_count as et_aoi_task_count
import eyetrack_spatial_error_time as et_spat_err
import eyetrack_aoi_participant_count
import eyetrack_aoi_histogram
import response_times_condition_boxplot as response_times


eyetrack_aoi_histogram.draw_plot('aoi_histogram_count.csv', 'eyetrack_aoi_histogram_count.png')
eyetrack_aoi_histogram.draw_plot('aoi_histogram_time.csv', 'eyetrack_aoi_histogram_time.png')

if False:
    # AOI Analysis
    et_aoi_task_count.draw_eyetrack_spatial_error_plot('aoi_task_comprehension_time_count.csv', 'eyetrack_aoi_task_python_count.png')
    eyetrack_aoi_task_count_bar.draw_eyetrack_spatial_error_plot('aoi_task_comprehension_count_bar.csv', 'eyetrack_aoi_task_python_count_bar.png')
    eyetrack_aoi_participant_count.draw_eyetrack_spatial_error_plot('aoi_task_participant_count.csv', 'eyetrack_aoi_participant_python_count.png')

    # Response Time
    response_times.draw_response_times_plot('ResponseTimeExport.csv', 'response_times.png')

    # Ogama
    et_spat_err.draw_eyetrack_spatial_error_plot('EyetrackSpatialErrorExport.csv', 'eyetrack_spatial_error_condition_ogama_raw.png')
    et_spat_err.draw_eyetrack_spatial_error_plot('EyetrackSpatialErrorExportWeighted.csv', 'eyetrack_spatial_error_condition_ogama_weighted.png')

    et_part.draw_eyetrack_spatial_error_plot('FixationRestAnalysisPartV2.csv', 'eyetrack_spatial_error_participants_ogama_weighted.png')

    et_part.draw_eyetrack_spatial_error_plot('FixationRestAnalysisPartV2.csv', 'eyetrack_spatial_error_participants_ogama_weighted_indiv_x.png', True, False, 'x')
    et_part.draw_eyetrack_spatial_error_plot('FixationRestAnalysisPartV2.csv', 'eyetrack_spatial_error_participants_ogama_weighted_indiv_y.png', True, False, 'y')

    # Python
    et_spat_err.draw_eyetrack_spatial_error_plot('EyetrackSpatialErrorPython.csv', 'eyetrack_spatial_error_condition_python_raw.png')
    et_spat_err.draw_eyetrack_spatial_error_plot('EyetrackSpatialErrorPythonWeighted.csv', 'eyetrack_spatial_error_condition_python_weighted.png')

    et_part.draw_eyetrack_spatial_error_plot('EyetrackSpatialErrorParticipantPython.csv', 'eyetrack_spatial_error_participants_python_raw.png')
    et_part.draw_eyetrack_spatial_error_plot('EyetrackSpatialErrorParticipantPython.csv', 'eyetrack_spatial_error_participants_python_raw_indiv_x.png', True, False, 'x')
    et_part.draw_eyetrack_spatial_error_plot('EyetrackSpatialErrorParticipantPython.csv', 'eyetrack_spatial_error_participants_python_raw_indiv_y.png', True, False, 'y')

    et_part.draw_eyetrack_spatial_error_plot('EyetrackSpatialErrorParticipantPythonWeighted.csv', 'eyetrack_spatial_error_participants_python_weighted.png')
    et_part.draw_eyetrack_spatial_error_plot('EyetrackSpatialErrorParticipantPythonWeighted.csv', 'eyetrack_spatial_error_participants_python_weighted_indiv_x.png', True, False, 'x')
    et_part.draw_eyetrack_spatial_error_plot('EyetrackSpatialErrorParticipantPythonWeighted.csv', 'eyetrack_spatial_error_participants_python_weighted_indiv_y.png', True, False, 'y')
