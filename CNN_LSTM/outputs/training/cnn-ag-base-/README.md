## TextAttack Model Card

This `cnn` model was fine-tuned for sequence classification using TextAttack
and the ag dataset loaded using the `datasets` library. The model was fine-tuned
for 10 epochs with a batch size of 64, a learning
rate of 0.01, and a maximum sequence length of 512.
Since this was a classification task, the model was trained with a cross-entropy loss function.
The best score the model achieved on this task was 0.8601666666666666, as measured by the
eval set accuracy, found after 4 epochs.

For more information, check out [TextAttack on Github](https://github.com/QData/TextAttack).
