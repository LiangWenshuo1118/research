
# GitHub 学习教程

GitHub 是一个非常强大的工具，对于软件开发和代码版本控制来说至关重要。本教程将帮助初学者了解和使用 GitHub 的基础功能。

## 第一部分：了解 GitHub

### 1. GitHub 是什么？
- **定义和功能**：GitHub 是一个基于 Git 的代码托管平台，用于版本控制和协作，允许多人在任何地方共同工作。

### 2. 基本概念
- **仓库（Repository）**：项目的存储位置。
- **分支（Branch）**：项目的不同版本。
- **提交（Commit）**：保存到仓库的更改。
- **拉取请求（Pull Request）**：告诉别人你已推送到仓库的分支上的更改。
- **合并（Merge）**：将更改加入主分支。

## 第二部分：创建 GitHub 账户和仓库

### 1. 注册 GitHub 账户
- 访问 [GitHub 官网](https://github.com) 并注册。

### 2. 创建新仓库
- 点击右上角的 "+" 图标，选择 "New repository"。
- 填写仓库名称和描述，选择是否公开或私有。
- 选择初始化仓库与 README 文件，这是项目的简介文件。

## 第三部分：Git 基础

### 1. 安装 Git
- 下载并安装 Git：

Linux：

```bash
sudo apt-get install git
```

### 2. 配置 Git
- 打开终端或命令提示符，配置用户信息：
  ```bash
  git config --global user.name "你的用户名"
  git config --global user.email "你的邮箱"
  ```
 ### 3. 克隆仓库
在仓库页面，点击 "Clone or download"，复制 URL。
在终端运行：
  ```bash
  git clone 你的仓库URL
  ```
 ### 4. 基本 Git 命令
- **git status**：查看更改状态。
- **git add**：跟踪文件更改。
- **git commit -m "提交信息"**：提交更新。
- **git push**：上传本地仓库内容到远程仓库。
  - **生成个人访问令牌的步骤**：
    1. 登录你的 GitHub 账户。
    2. 点击右上角的头像，然后选择 "Settings"（设置）。
    3. 在侧边栏中，找到并点击 "Developer settings"（开发者设置）。
    4. 在左侧菜单中选择 "Personal access tokens"（个人访问令牌）。
    5. 点击 "Generate new token"（生成新令牌）。
    6. 给你的令牌命名，并设置过期时间。然后选择你需要的权限。如果你只需要用于代码仓库的操作，通常选择 `repo` 权限即可。
    7. 点击页面底部的 "Generate token"（生成令牌）。
    8. **确保复制你的新令牌**。你只能在这个时候看到它一次。使用此令牌作为密码进行认证。
- **git pull**：更新远程仓库到本地仓库。

  
## 第四部分：探索和贡献
### 1. 探索开源项目
- GitHub Explore：查找和参与开源项目。
### 2. 贡献到项目
- Fork 和 Clone 项目。
- 创建新分支，进行更改。
- 提交拉取请求。
## 第五部分：使用 GitHub 的高级功能
### 1. GitHub Pages
- 托管个人或项目网站。
### 2. GitHub Actions
- 自动化工作流程，如持续集成和持续部署。
