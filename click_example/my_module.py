
from typing import Dict

from click_example.base_module import BaseModule

FileRef = str
Output = str

class TestModule(BaseModule):
    def run_job_logic(self, parameters: Dict, files: Dict[str, FileRef]) -> Output:
        print("helo from test module.")
