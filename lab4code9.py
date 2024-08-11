# A9: Confusion Matrix and Performance Metrics
confuse = confusion_matrix(Y_test, pred)
precisions = precision_score(y_test, pred, average='macro')
recall = recall_score(y_test, pred, average='macro')
f1 = f1_score(Y_test, pred, average='macro')

print("The Confusion Matrix:\n", confuse)
print("Precision matrix:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
