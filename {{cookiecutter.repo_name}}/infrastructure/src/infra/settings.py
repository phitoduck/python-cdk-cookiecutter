"""Define the settings needed to run `cdk <subcommand> path/to/app.py`."""

from functools import cached_property

import aws_cdk as cdk
from pydantic import Field
from pydantic import BaseSettings
import boto3


class Settings(BaseSettings):
    """
    Define the settings needed to deploy this app and infrastructure to AWS.

    The attributes of this class will be read from environment variables (case insensitive).

    Inheritance tree of this class: `pydantic.BaseModel` <- `pydantic.BaseSettings` <- THIS
    See the docs here: https://docs.pydantic.dev/usage/validators/
    """

    aws_region: str = Field("us-west-2", description="The AWS region to deploy to.")
    stack_name = "{{ cookiecutter.repo_name }}"

    class Config:
        """
        Pydantic model config.
        
        Find the available configuration options here:
        https://docs.pydantic.dev/latest/usage/model_config/#options
        """

        # Attribute "SOME_FIELD" would be the same as "some_field" in env vars
        case_sensitive = False

        # Prevent errors if non-Pydantic models are used as field values
        arbitrary_types_allowed = True

        # Nested Pydantic models are supported in BaseSettings, e.g.
        # Setting "X__Y__Z=a" results in `base_settings_instance.x.y.z == "a"` being true.
        env_nested_delimiter = "__"

        # needed because setting aws_account_id as a cached_property was causing an error
        keep_untouched = (cached_property,)

    @cached_property
    def aws_account_id(self) -> str:
        """
        Derive the AWS account ID to deploy to.

        The account ID is derived from any of these places:

        - The ``AWS_PROFILE`` environment variable
        - The ``AWS_ACCESS_KEY_ID`` and ``AWS_SECRET_ACCESS_KEY`` environment variables
        """
        return boto3.client("sts").get_caller_identity().get("Account")

    @cached_property
    def cdk_env(self) -> cdk.Environment:
        """Get the CDK environment dict for this app."""
        return cdk.Environment(
            account=self.aws_account_id,
            region=self.aws_region,
        )
    
    def dict(self, *args, **kwargs) -> dict:
        """Generate a dictionary representation of the model, optionally specifying which fields to include or exclude."""
        to_return: dict = super(BaseSettings, self).dict(*args, **kwargs)
        to_return["cdk_env"] = self.cdk_env
        to_return["aws_account_id"] = self.aws_account_id
        return to_return
