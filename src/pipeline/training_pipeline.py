from src.pipeline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline,
)

from src.pipeline.stage_02_data_validation import (
    DataValidationTrainingPipeline,
)

from src.pipeline.stage_03_data_transformation import (
    DataTransformationTrainingPipeline,
)

from src.pipeline.stage_04_model_training import (
    ModelTrainingPipeline,
)

from src.pipeline.stage_05_model_evaluation import (
    ModelEvaluationPipeline,
)


class TrainingPipeline:

    def __init__(self):
        pass

    def run_pipeline(self):

        DataIngestionTrainingPipeline().main()

        DataValidationTrainingPipeline().main()

        DataTransformationTrainingPipeline().main()

        ModelTrainingPipeline().main()

        ModelEvaluationPipeline().main()
