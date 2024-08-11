# A8 varying k
a = []
for k in range(1, 13-1):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, Y_train)
    acc = knn.score(X_test, Y_test)
    a.append(acc)

plt.plot(range(1, 12), a)
plt.xlabel('k')
plt.ylabel('Accuracy')
plt.title('k-NN Accuracy for varying k')
plt.show()
