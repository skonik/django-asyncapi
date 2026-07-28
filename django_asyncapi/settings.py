from pydantic import BaseModel, Field, ImportString


class DjangoAsyncapiSettings(BaseModel):
    ASYNCAPI_SPEC_CLASS: list[ImportString] | ImportString = Field(
        ...,
        description="Path to class containing entrypoint for defining root of asyncapi specification"
    )
