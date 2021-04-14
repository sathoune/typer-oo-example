import abc
from typing import Dict

from .utils import option, command, Cli
FileRef = str
Output = str
def ClickPath(exists=str):
    return str


class BaseModule(abc.ABC, Cli):

    @abc.abstractmethod
    def run_job_logic(self, parameters: Dict, files: Dict[str, FileRef]) -> Output:
        """
        This is the custom implementation of what will become an interface. Does the necessary setup
        to execute the existing module code. This method should represent 90% or more of the custom code
        required to create a module using pre existing logic.

        Arguments:
            parameters {dict} -- [description]
            files {dict} -- [description]
            output_path {str} -- [description]
        """
        pass


    @command("run-job")
    @option(
        "params_path",
        "--params-path",
        default=None,
        envvar="PARAMS_PATH",
        type=ClickPath(exists=True),
    )
    @option(
        "params_json", "--params-json", default=None, envvar="PARAMS_JSON", type=str
    )
    @option(
        "file_refs_json",
        "--files-json",
        default=None,
        envvar="FILE_REFS_JSON",
        type=str,
    )
    @option(
        "file_refs_path",
        "--files-path",
        default=None,
        envvar="FILE_REFS_PATH",
        type=ClickPath(exists=True),
    )
    @option(
        "input_path",
        "--input",
        default="input",
        envvar="FILES_IN_PATH",
        type=ClickPath(),
    )
    @option(
        "output_path",
        "--output",
        default="output",
        envvar="OUTPUT_PATH",
        type=ClickPath(),
    )
    @option("--zip", is_flag=True)
    def run_job(
        self,
        params_path,
        params_json,
        file_refs_json,
        file_refs_path,
        input_path,
        output_path,
        zip,
    ):
        print('Hello from base module.')
        self.run_job_logic({}, {})