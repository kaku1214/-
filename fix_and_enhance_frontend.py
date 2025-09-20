import os
import re

# 文件路径
html_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html')

# 读取文件内容
with open(html_file_path, 'r', encoding='utf-8', errors='ignore') as file:
    content = file.read()

# 1. 修复JavaScript错误 - 删除错误的Python命令，只保留showStep(1);
# 搜索错误模式并替换
fixed_content = re.sub(r'python -m http.server 8000python -m http.server 8000\s+showStep\(1\);', 'showStep(1);', content)

# 2. 添加代码输入功能和弹出系统流程
# 在DOMContentLoaded事件监听器前添加一个模态框用于代码输入
modal_code = '''
        // 代码输入模态框
        function createCodeInputModal() {
            const modalHTML = `
            <div id="code-input-modal" class="fixed inset-0 z-50 flex items-center justify-center hidden">
                <div class="absolute inset-0 bg-black bg-opacity-50" id="modal-backdrop"></div>
                <div class="relative bg-white rounded-xl shadow-xl w-full max-w-md p-6">
                    <h2 class="text-xl font-bold text-gray-900 mb-4">请输入访问代码</h2>
                    <div class="mb-4">
                        <label for="access-code" class="block text-sm font-medium text-gray-700 mb-1">访问代码</label>
                        <input type="text" id="access-code" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-primary" placeholder="请输入4位数代码">
                        <p id="code-error" class="mt-1 text-sm text-red-600 hidden">代码错误，请重新输入</p>
                    </div>
                    <div class="flex justify-end space-x-3">
                        <button id="close-code-modal" class="px-4 py-2 bg-gray-200 text-gray-800 font-medium rounded-lg hover:bg-gray-300 transition-smooth">
                            取消
                        </button>
                        <button id="submit-code" class="px-4 py-2 bg-primary text-white font-medium rounded-lg hover:bg-primary/90 transition-smooth">
                            确认
                        </button>
                    </div>
                </div>
            </div>
            `;
            
            // 将模态框添加到body
            document.body.insertAdjacentHTML('beforeend', modalHTML);
            
            // 添加事件监听器
            document.getElementById('submit-code').addEventListener('click', checkAccessCode);
            document.getElementById('close-code-modal').addEventListener('click', () => {
                document.getElementById('code-input-modal').classList.add('hidden');
            });
            document.getElementById('modal-backdrop').addEventListener('click', () => {
                document.getElementById('code-input-modal').classList.add('hidden');
            });
            
            // 添加回车键支持
            document.getElementById('access-code').addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    checkAccessCode();
                }
            });
        }
        
        // 检查访问代码
        function checkAccessCode() {
            const accessCode = document.getElementById('access-code').value.trim();
            const validCodes = ['1234', '5678', '9999', '0000']; // 示例有效代码
            
            if (validCodes.includes(accessCode)) {
                document.getElementById('code-input-modal').classList.add('hidden');
                document.getElementById('access-code').value = '';
                showSystemProcess(); // 显示系统流程
            } else {
                document.getElementById('code-error').classList.remove('hidden');
                // 2秒后隐藏错误提示
                setTimeout(() => {
                    document.getElementById('code-error').classList.add('hidden');
                }, 2000);
            }
        }
        
        // 显示系统流程
        function showSystemProcess() {
            const processModalHTML = `
            <div id="process-modal" class="fixed inset-0 z-50 flex items-center justify-center hidden">
                <div class="absolute inset-0 bg-black bg-opacity-50" id="process-backdrop"></div>
                <div class="relative bg-white rounded-xl shadow-xl w-full max-w-2xl p-6">
                    <h2 class="text-xl font-bold text-gray-900 mb-4">篮球鞋推荐系统流程</h2>
                    <div class="space-y-4 mb-4">
                        <div class="flex items-start">
                            <div class="flex-shrink-0 w-8 h-8 rounded-full bg-primary text-white flex items-center justify-center font-medium mt-1">1</div>
                            <div class="ml-3">
                                <h3 class="text-lg font-medium text-gray-900">填写基本信息</h3>
                                <p class="mt-1 text-sm text-gray-600">输入您的打球位置、体重和打球风格</p>
                            </div>
                        </div>
                        <div class="flex items-start">
                            <div class="flex-shrink-0 w-8 h-8 rounded-full bg-primary text-white flex items-center justify-center font-medium mt-1">2</div>
                            <div class="ml-3">
                                <h3 class="text-lg font-medium text-gray-900">完成测评问卷</h3>
                                <p class="mt-1 text-sm text-gray-600">回答关于您的鞋款偏好和特殊需求的问题</p>
                            </div>
                        </div>
                        <div class="flex items-start">
                            <div class="flex-shrink-0 w-8 h-8 rounded-full bg-primary text-white flex items-center justify-center font-medium mt-1">3</div>
                            <div class="ml-3">
                                <h3 class="text-lg font-medium text-gray-900">获取个性化推荐</h3>
                                <p class="mt-1 text-sm text-gray-600">系统将根据您的信息生成专属篮球鞋推荐列表</p>
                            </div>
                        </div>
                    </div>
                    <div class="flex justify-center">
                        <button id="close-process-modal" class="px-6 py-2 bg-primary text-white font-medium rounded-lg hover:bg-primary/90 transition-smooth">
                            开始使用
                        </button>
                    </div>
                </div>
            </div>
            `;
            
            // 将流程模态框添加到body
            document.body.insertAdjacentHTML('beforeend', processModalHTML);
            
            // 显示流程模态框
            document.getElementById('process-modal').classList.remove('hidden');
            
            // 添加关闭按钮事件
            document.getElementById('close-process-modal').addEventListener('click', () => {
                document.getElementById('process-modal').classList.add('hidden');
                // 滚动到测评区域
                document.querySelector('#start').scrollIntoView({ behavior: 'smooth' });
            });
            document.getElementById('process-backdrop').addEventListener('click', () => {
                document.getElementById('process-modal').classList.add('hidden');
            });
        }
        
        // 添加代码输入按钮到导航栏
        function addCodeInputButton() {
            const navElement = document.querySelector('nav div.flex.justify-between');
            if (navElement) {
                const rightSection = navElement.lastElementChild;
                const buttonHTML = `
                <button id="open-code-input" class="md:inline-flex px-3 py-2 ml-4 rounded-md text-sm font-medium text-white bg-accent hover:bg-accent/90 transition-smooth">
                    输入代码 <i class="fa fa-key ml-1"></i>
                </button>
                `;
                rightSection.insertAdjacentHTML('beforeend', buttonHTML);
                
                // 添加点击事件
                document.getElementById('open-code-input').addEventListener('click', () => {
                    document.getElementById('code-input-modal').classList.remove('hidden');
                });
            }
        }
'''

# 在DOMContentLoaded事件监听器前插入新功能代码
fixed_content = re.sub(r'(document\.addEventListener\(\'DOMContentLoaded\', \(\) => \{)', modal_code + '\n        \1', fixed_content)

# 在DOMContentLoaded事件监听器内部添加初始化代码
fixed_content = re.sub(r'(// 确保新手问题显示)', '            // 创建代码输入模态框\n            createCodeInputModal();\n            // 添加代码输入按钮\n            addCodeInputButton();\n\n            \1', fixed_content)

# 保存修复后的文件
with open(html_file_path, 'w', encoding='utf-8') as file:
    file.write(fixed_content)

print(f"已成功修复 {html_file_path} 中的JavaScript错误并添加了代码输入功能")
print("修复内容：")
print("1. 删除了错误的Python命令，保留了正确的showStep(1);代码")
print("2. 添加了代码输入模态框功能")
print("3. 添加了系统流程展示功能")
print("4. 在导航栏添加了代码输入按钮")
print("\n有效访问代码示例：1234, 5678, 9999, 0000")