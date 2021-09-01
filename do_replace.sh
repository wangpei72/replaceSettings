#!/usr/bin/env bash
echo "job starting..."
repo_name_list=(
  biz_desktop
)
prefix="$1"
len=${#repo_name_list[*]}
echo "repo nums in total: ${len}"
for((i=0;i<$len;i++));do
    echo -e "\033[37;41m now is doing job for ${repo_name_list[$i]}... \033[0m";
    # 进入仓库目录 创建分支
    # git checkout -B <branch> <remote>
    cd ${prefix}/${repo_name_list[$i]}
    git checkout -B feature/upgrade_target30 origin/develop
    
    # 执行替换
    /Users/wangpei/workspace/replaceSettings/workFlow.py -p ${prefix} -n ${repo_name_list[$i]}
    
    # git 提交
    git add.
    git commit -m "feature:执行do_replace.sh脚本,替换构建参数文本"
    
    # git push <remote> <branch>:<branch-rm>
    git push origin feature/upgrade_target30:feature/upgrade_target30
    echo -e "\033[37;41m done job for ${repo_name_list[$i]}... \033[0m"
done
echo -e  "\033[33;44m job done. \033[0m"