import os

def mkdir(path):
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print('create new folder success!')
        return True
    else:
        print('folder already existed!')
        return False

    
results_path = '~/playground/projects/fangyubo/pyserini/runs/results_v3'

qid = 0
query = {'sub_len_label':'test_long', 'sub_readability':'test_plain'}

result_path = results_path + "/" + f"{qid}" + "/" + f"{query['sub_len_label']}_{query['sub_readability']}"

print(mkdir(result_path))