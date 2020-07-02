
import json
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, fbeta_score

with open('Evaluation.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    true = data['label']
    pred =  data['predict']

def eval(true, pred):
    ave = ['macro', 'micro']
    precision = []
    recall = []
    fbeta = []
    f1 = []
    acc = accuracy_score(true, pred)
    for i in ave:
        precision.append(precision_score(true, pred, average=i))
        recall.append(recall_score(true, pred, average=i))
        f1.append(f1_score(true, pred, average=i))
    return acc, precision, recall, f1

conf_mat = confusion_matrix(true, pred)
evaluation = eval(true, pred)
save_file_name = '2019711752_윤민형_EVAL'
with open('./'+save_file_name+'.txt', 'w', encoding='utf-8', newline='') as writer_text:
    writer_text.writelines('Confusion martix' + '\n')
    for i in conf_mat:
        for j in i:
            writer_text.writelines(str(j) + '\t')
        writer_text.writelines('\n')
    writer_text.writelines('\n')
    writer_text.writelines('Accuracy : ' + str(evaluation[0]*100) +'%' + '\n')
    writer_text.writelines('\n')
    list = ['precision', 'recall', 'f1-score']
    for idx, k in enumerate(range(len(evaluation[1:]))):
        writer_text.writelines('Macro average ' + str(list[idx]) +' : ' 
                               + str(evaluation[k+1][0]*100) +'%' + '\n')
        writer_text.writelines('Micro averate ' + str(list[idx]) +' : ' 
                               + str(evaluation[k+1][1]*100) +'%'+ '\n\n')
    #writer_text.close()
    print("[저장 완료]")

