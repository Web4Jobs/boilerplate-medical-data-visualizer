import capture_results
capture_results.start()

import medical_data_visualizer
from unittest import main
import traceback

program = None
runtime_error = None

try:
    medical_data_visualizer.draw_cat_plot()
    medical_data_visualizer.draw_heat_map()

    program = main(module="test_module", exit=False)

except Exception as e:
    runtime_error = e
    traceback.print_exc()

finally:
    capture_results.finish(program, runtime_error)