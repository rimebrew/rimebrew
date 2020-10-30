from typing import Union, Dict, List

sample = \
    """
    jobs:
      build:
        docker:
          - image: circleci/<language>:<version TAG>
            auth:
              username: mydockerhub-user
              password: $DOCKERHUB_PASSWORD  # context / project UI env-var reference
        steps:
          - checkout
          - run: echo "this is the build job"
      test:
        docker:
          - image: circleci/<language>:<version TAG>
            auth:
              username: mydockerhub-user
              password: $DOCKERHUB_PASSWORD  # context / project UI env-var reference
        steps:
          - checkout
          - run: echo "this is the test job"
    
    # Orchestrate our job run sequence
    workflows:
      build_and_test:
        jobs:
          - build
          - test
    """


class yaml_tree:
    """
    A parsed yaml tree is different than other trees:
    mixed data type -> dict or list
    """

    def __init__(self, yaml: Union[List, Dict]):
        self.yaml = yaml;

    def show_entry(self, yPath: str):
        pass

    def add_entry(self, yPath: str):
        """
        yPath follow this pattern:
        "xxx/yyy/the entry"
        """
        pass


# the lines below is a mini sed editor


# 😎😎😎😎😎😎
# An advanced functional programming paradigm
# In in python you can return a FUNCTION
#
# The xpath sub lang used by RIME
#
# "一級設定項/二級設定項/三級設定項": 新的設定值
# "另一個設定項": 新的設定值
# "再一個設定項": 新的設定值
# "含列表的設定項/@n": 列表第n個元素新的設定值，從0開始計數
# "含列表的設定項/@last": 列表最後一個元素新的設定值
# "含列表的設定項/@before 0": 在列表第一個元素之前插入新的設定值（不建議在補靪中使用）
# "含列表的設定項/@after last": 在列表最後一個元素之後插入新的設定值（不建議在補靪中使用）
# "含列表的設定項/@next": 在列表最後一個元素之後插入新的設定值（不建議在補靪中使用）
# "含列表的設定項/+": 與列表合併的設定值（必須爲列表）
# "含字典的設定項/+": 與字典合併的設定值（必須爲字典，注意YAML字典的無序性）

# a function can be determined by callable()

def ypath(_str: str):
    head = '/'
    for token in _str.split(head):
        if token in set('+'):
            yield lambda x: print('append')
        else:
            yield token


for i in ypath('patch/schema_list/+'):
    print(i)

yml = yaml_tree(sample)
