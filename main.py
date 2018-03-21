import eyetrack_spatial_participants as et_part
import eyetrack_spatial_error_time as et_spat_err
import response_times_condition_boxplot as response_times

response_times.draw_response_times_plot('ResponseTimeExport.csv', 'response_times.png')

et_spat_err.draw_eyetrack_spatial_error_plot('EyetrackSpatialErrorExport.csv', 'eyetrack_spatial_error.png')
et_spat_err.draw_eyetrack_spatial_error_plot('EyetrackSpatialErrorExportWeighted.csv', 'eyetrack_spatial_error_weighted.png')

et_part.draw_eyetrack_spatial_error_plot('FixationRestAnalysisPartV2.csv', 'eyetrack_spatial_error_part_weighted.png')

et_part.draw_eyetrack_spatial_error_plot('FixationRestAnalysisPartV2.csv', 'eyetrack_spatial_error_part_weighted_indiv_x.png', True, False, 'x')
et_part.draw_eyetrack_spatial_error_plot('FixationRestAnalysisPartV2.csv', 'eyetrack_spatial_error_part_weighted_indiv_y.png', True, False, 'y')
