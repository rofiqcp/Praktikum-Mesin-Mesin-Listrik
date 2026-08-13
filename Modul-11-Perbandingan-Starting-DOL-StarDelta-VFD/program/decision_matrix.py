options = {
    'DOL': [5, 1, 1, 5],
    'STAR-DELTA': [2, 3, 1, 3],
    'VFD': [4, 5, 5, 2],
}
weights = [5, 4, 3, 2]
labels = ['torque', 'current', 'speed_control', 'simplicity']

print('criteria =', labels)
print('weights  =', weights)
results = {}
for name, values in options.items():
    total = sum(w * v for w, v in zip(weights, values))
    results[name] = total
    print(f'{name:12s} values={values} weighted_score={total}')

print('highest example score =', max(results, key=results.get))
print('Edit weights for the assigned academic case and explain the choice.')
