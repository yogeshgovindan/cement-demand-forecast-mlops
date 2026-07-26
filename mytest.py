# # import pandas as pd

# # df = pd.read_csv(
# #     "artifacts/data_transformation/test.csv"
# # )

# # print(df.columns.tolist())


# import mlflow

# mlflow.set_tracking_uri(
#     "sqlite:///mlflow.db"
# )

# client = mlflow.tracking.MlflowClient()

# model = client.get_registered_model(
#     "cement_demand_model"
# )

# for version in model.latest_versions:
#     print("Version:", version.version)
#     print("Source:", version.source)


# import mlflow

# mlflow.set_tracking_uri(
#     "sqlite:///mlflow.db"
# )

# client = mlflow.tracking.MlflowClient()

# version = client.get_model_version(
#     name="cement_demand_model",
#     version="2"
# )

# print("Model Version:")
# print(version)

# print("\nSource:")
# print(version.source)

# print("\nRun ID:")
# print(version.run_id)


# run = client.get_run(
#     version.run_id
# )

# print("\nArtifact URI:")
# print(run.info.artifact_uri)

import mlflow

mlflow.set_tracking_uri("sqlite:///mlflow.db")

client = mlflow.tracking.MlflowClient()

version = client.get_model_version(
    name="cement_demand_model",
    version="1"
)

print("Version:", version.version)
print("Source:", version.source)
print("Run ID:", version.run_id)

run = client.get_run(version.run_id)

print("Artifact URI:", run.info.artifact_uri)
