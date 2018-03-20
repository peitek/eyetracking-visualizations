import eyetrack_spatial_error_time_absolute as et_spat_err
import response_times_condition_boxplot as response_times

response_times.draw_response_times_plot('ResponseTimeExport.csv', 'response_times.png')

et_spat_err.draw_eyetrack_spatial_error_plot('EyetrackSpatialErrorExport.csv', 'eyetrack_spatial_error.png')
et_spat_err.draw_eyetrack_spatial_error_plot('EyetrackSpatialErrorExportWeighted.csv', 'eyetrack_spatial_error_weighted.png')