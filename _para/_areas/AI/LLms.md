How are models trained
Pre training
Post training
- Uses technique called reinforcement learning. Model creates an answer, the answer is scored and then the model is nudged.
- How are the scores generated?
1. RLHF - humans score it. Downside is that it can learn to 
2. RLVR - variable rewared. Does the code pass the unit tests. does the math get solved

Jev is trained with
3. RLCD - Calibrated decisions
Calibrated
- Well calibrated model has probability and correctness with a linear relationship
- When we say 80% probability, we know its correct 80% of the time