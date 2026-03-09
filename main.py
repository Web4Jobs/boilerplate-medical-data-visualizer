import capture_results  # ✅ new
capture_results.start()  # ✅ new (start capture)

import medical_data_visualizer
from unittest import main

# Test your function by calling it here
medical_data_visualizer.draw_cat_plot()
medical_data_visualizer.draw_heat_map()

# Run unit tests automatically
program = main(module="test_module", exit=False)  # ✅ new: capture program
capture_results.finish(program)                  # ✅ new: write results