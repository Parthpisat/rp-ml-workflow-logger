import uuid
from pydantic import BaseModel, Field
from typing import Dict, Any
from ml_workflow_logger.models.flow import Flow
from ml_workflow_logger.models.run import Run


class FlowRecord(BaseModel):
   id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias='_id')
    # TODO: Fill out the other records you need to have to make this a standardized record
    # TODO: Create a reference to the Flow model, Run model, and any other models you need
   step_name: str
   step_data: Dict[str, Any]
   flow_ref: Flow
   run_ref: Run

   def to_dict(self) -> Dict[str, Any]:
      return self.Dict(by_alias=True, exclude_none=True)

