## TextAttack Model Card

This `lstm_mask` model was fine-tuned for sequence classification using TextAttack
and the ag dataset loaded using the `datasets` library. The model was fine-tuned
for 30 epochs with a batch size of 64, a learning
rate of 0.005, and a maximum sequence length of 512.
Since this was a classification task, the model was trained with a cross-entropy loss function.
The best score the model achieved on this task was 0.8961666666666667, as measured by the
eval set accuracy, found after 26 epochs.

For more information, check out [TextAttack on Github](https://github.com/QData/TextAttack).
