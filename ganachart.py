import pandas as pd
import plotly.express as px

df = pd.DataFrame([
    dict(Task = "Outcome 1", Start = '2023-06-26', End = '2023-07-02', Assigned = "Person D", Difficulty = 57),
    dict(Task = "Activity 1.1", Start = '2023-06-26', End = '2023-06-28', Assigned = "Person A", Difficulty = 70),
    dict(Task = "Activity 1.2", Start = '2023-06-28', End = '2023-06-30', Assigned = "Person B", Difficulty = 20),
    dict(Task = "Activity 1.3", Start = '2023-06-30', End = '2023-07-02', Assigned = "Person C", Difficulty = 80),
    dict(Task = "Outcome 2", Start = '2023-07-02', End = '2023-07-09', Assigned = "Person H", Difficulty = 87),
    dict(Task = "Activity 2.1", Start = '2023-07-02', End = '2023-07-04', Assigned = "Person E", Difficulty = 90),
    dict(Task = "Activity 2.2", Start = '2023-07-04', End = '2023-07-06', Assigned = "Person F", Difficulty = 90),
    dict(Task = "Activity 2.3", Start = '2023-07-06', End = '2023-07-09', Assigned = "Person G", Difficulty = 80),
    dict(Task = "Outcome 3", Start = '2023-07-09', End = '2023-07-16', Assigned = "Person L", Difficulty = 93),
    dict(Task = "Activity 3.1", Start = '2023-07-09', End = '2023-07-11', Assigned = "Person I", Difficulty = 90),
    dict(Task = "Activity 3.2", Start = '2023-07-11', End = '2023-07-13', Assigned = "Person G", Difficulty = 90),
    dict(Task = "Activity 3.3", Start = '2023-07-13', End = '2023-07-16', Assigned = "Person K", Difficulty = 100),
])


fig = px.timeline(df, x_start = "Start", x_end = "End", y = "Task",
                  color = "Difficulty", color_continuous_scale = "viridis")
# Tasks from top to bottom
fig.update_yaxes(autorange = "reversed") 
fig.update_layout(
    title="3 week time line",
    font=dict(size=30, family="Arial"),
    title_x=0.5
)
fig.show()


# import pandas as pd
# import plotly.express as px

# df = pd.DataFrame([
#     dict(Task = "Outcome 1", Start = '1', End = '7', Assigned = "Person D", Difficulty = 57),
#     dict(Task = "Activity 1", Start = '1', End = '3', Assigned = "Person A", Difficulty = 70),
#     dict(Task = "Activity 2", Start = '3', End = '5', Assigned = "Person B", Difficulty = 20),
#     dict(Task = "Activity 3", Start = '5', End = '7', Assigned = "Person C", Difficulty = 80),
#     dict(Task = "Outcome 2", Start = '7', End = '14', Assigned = "Person H", Difficulty = 87),
#     dict(Task = "Activity 2.1", Start = '7', End = '10', Assigned = "Person E", Difficulty = 90),
#     dict(Task = "Activity 2.2", Start = '10', End = '12', Assigned = "Person F", Difficulty = 90),
#     dict(Task = "Activity 2.3", Start = '12', End = '14', Assigned = "Person G", Difficulty = 80),
#     dict(Task = "Outcome 3", Start = '14', End = '21', Assigned = "Person L", Difficulty = 93),
#     dict(Task = "Activity 3.1", Start = '14', End = '16', Assigned = "Person I", Difficulty = 90),
#     dict(Task = "Activity 3.2", Start = '16', End = '19', Assigned = "Person G", Difficulty = 90),
#     dict(Task = "Activity 3.3", Start = '19', End = '21', Assigned = "Person K", Difficulty = 100),
# ])


# fig = px.timeline(df, x_start = "Start", x_end = "End", y = "Task",
#                   color = "Difficulty", color_continuous_scale = "viridis")
# # Tasks from top to bottom
# fig.update_yaxes(autorange = "reversed") 

# fig.update_xaxes(
#     tickmode='linear',
#     tick0=0,
#     dtick=1,
#     tickformat='d'
# )

# fig.update_layout(
#     font=dict(size=30, family="Arial")
# )
# fig.show()