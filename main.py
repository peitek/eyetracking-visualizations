import eyetrack_spatial_participants as et_part
import eyetrack_spatial_error_time as et_spat_err
import response_times_condition_boxplot as response_times

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