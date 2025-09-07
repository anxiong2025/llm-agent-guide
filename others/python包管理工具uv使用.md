
Astral Software 公司不仅发布 ruff 爆款 python linter 工具，还发布 uv 一款由 Rust 编写的高性能 Python 包管理工具，简直太炸裂了。

可以替代 pip、pip-tools、pipx、poetry、pyenv、twine、virtualenv 等。。。

https://github.com/astral-sh/uv

https://github.com/astral-sh/ruff

基本使用

```python3
#1 初始化项目，管理依赖
uv init hello-world

#cd hello-world
uv add 'requests==2.32.5' # 增加依赖
uv lock --upgrade-package requests # 更新项目依赖
uv remove requests # 删除项目依赖
```

用 uv 创建虚拟环境

```python

uv venv #参数可选，e.g uv venv --python 3.11

### 激活虚拟环境
source .venv/bin/activate

### 同步项目依赖,项目已经有 `pyproject.toml`和 `uv.lock`文件，激活虚拟环境后，使用命令来安装所有依赖项，确保环境与锁文件一致
uv sync
```

项目结构

```sh
total 48
drwxr-xr-x@ 8 robert  staff    256  9  7 11:23 .
drwxr-xr-x@ 4 robert  staff    128  9  7 11:19 ..
-rw-r--r--@ 1 robert  staff      5  9  7 11:19 .python-version
drwxr-xr-x@ 8 robert  staff    256  9  7 11:23 .venv
-rw-r--r--@ 1 robert  staff      0  9  7 11:19 README.md
-rw-r--r--@ 1 robert  staff     89  9  7 11:19 main.py
-rw-r--r--@ 1 robert  staff    182  9  7 11:20 pyproject.toml
-rw-r--r--@ 1 robert  staff  11344  9  7 11:20 uv.lock
```


