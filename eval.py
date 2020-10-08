import os
import pandas as pd

querys_path = '~/playground/projects/fangyubo/pyserini/collections/query_dev_pairs.csv'
eval_path = '~/work/anserini/tools/scripts/msmarco/msmarco_eval.py'
qrel_path = '~/shared/Datasets/MSMARCO/MSMARCO-Deep-Learning/qrels.dev.small.tsv'
results_path = '~/playground/projects/fangyubo/pyserini/runs/results_v3'
#result_path = '/1081338/long_easy/result.tsv'
eval_results_path = '/home/jovyan/playground/projects/fangyubo/pyserini/runs/eval_results.txt'

# read in all querys
querys = pd.read_csv(querys_path)

def result_process(path):
    result = pd.read_csv(f'{path}/result.csv')
    result = result[['qid', 'pid', 'rank']]
    result.to_csv(f'{path}/result.tsv',sep='\t',index=0,header=0)
    
for i in range(querys.shape[0]):
    try:
        query = querys.loc[i, :]
        qid = query['qid']
        length = query['sub_len_label']
        readability = query['sub_readability']
        result_path = f'/{qid}/{length}_{readability}'
        result_process(f'{results_path}{result_path}')
        processed_result_path = f'/{qid}/{length}_{readability}/result.tsv'

        cmd = f'python {eval_path} {qrel_path} {results_path}{processed_result_path}'

        eval_result = os.popen(cmd).readlines()
        with open(eval_results_path, 'a') as f:
            f.write(f'{qid}\t{length}\t{readability}\n')
            f.write(eval_result[1])|f.write(eval_result[2])
            f.write('\n')
        print(f'{qid}\t{length}\t{readability}:evaluated!')
    except:
        continue