# ccf_paddle
detail:https://aistudio.baidu.com/aistudio/competition/detail/115/0/introduction
train
> python main.py -c configs/recognition/agcn/agcn_fsd.yaml  --validate

test
> python main.py --test -c configs/recognition/agcn/agcn_fsd.yaml -w output/AGCN/AGCN_best.pdparams

