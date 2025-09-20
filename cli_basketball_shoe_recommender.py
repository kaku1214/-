#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
篮球鞋推荐系统命令行版本
为用户提供基于个人特征、打球风格和偏好的篮球鞋推荐
"""

import os
import time
from typing import Dict, List, Tuple, Any

class BasketballShoeRecommender:
    """篮球鞋推荐系统类"""
    
    def __init__(self):
        """初始化推荐系统"""
        # 风格类型定义
        self.style_types = [
            {"name": "力量内线型", "en": "Power Inside"},
            {"name": "快速突破型", "en": "Quick Drive"},
            {"name": "精准投篮型", "en": "Sharp Shooter"},
            {"name": "全面均衡型", "en": "All-Around"},
            {"name": "组织传球型", "en": "Playmaker"},
            {"name": "防守专家型", "en": "Defensive Specialist"},
            {"name": "团队配合型", "en": "Team Player"}
        ]
        
        # 球鞋数据
        self.shoes_data = self._load_shoes_data()
        
        # 用户数据
        self.user_data = {}
        
        # 风格分析结果
        self.style_analysis = {}
        
        # 推荐结果
        self.recommendations = []
    
    def _load_shoes_data(self) -> List[Dict[str, Any]]:
        """加载球鞋数据"""
        return [
            # 全能均衡型
            {"name": "Nike Air Zoom BB NXT", "brand": "耐克/Nike", "price": 1399, "type": "全面均衡型", "position": "全位置", "court_type": "室内木地板", "foot_type": "正常脚型", "cushioning": 9, "support": 8, "lightweight": 8, "durability": 7, "traction": 9, "breathability": 8, "link": "https://www.nike.com/cn/t/air-zoom-bb-nxt-basketball-shoes-9FjP9h/CD5007-100"},
            {"name": "Adidas D.O.N. Issue 3", "brand": "阿迪达斯/Adidas", "price": 999, "type": "全面均衡型", "position": "全位置", "court_type": "室内木地板", "foot_type": "正常脚型", "cushioning": 8, "support": 9, "lightweight": 7, "durability": 8, "traction": 9, "breathability": 7, "link": "https://www.adidas.com.cn/don-issue-3-g57915"},
            {"name": "Li-Ning CJ1", "brand": "李宁", "price": 899, "type": "全面均衡型", "position": "全位置", "court_type": "室内木地板", "foot_type": "正常脚型", "cushioning": 9, "support": 8, "lightweight": 8, "durability": 7, "traction": 8, "breathability": 8, "link": "https://lining.tmall.com/p/rd281245.htm"},
            {"name": "Nike LeBron Witness 6", "brand": "耐克/Nike", "price": 899, "type": "全面均衡型", "position": "全位置", "court_type": "室内木地板", "foot_type": "正常脚型", "cushioning": 8, "support": 9, "lightweight": 6, "durability": 9, "traction": 8, "breathability": 7, "link": "https://www.nike.com/cn/t/lebron-witness-6-basketball-shoes-14C5M7/CW3155-100"},
            {"name": "Adidas Harden Vol. 5", "brand": "阿迪达斯/Adidas", "price": 1299, "type": "全面均衡型", "position": "全位置", "court_type": "室内木地板", "foot_type": "正常脚型", "cushioning": 9, "support": 8, "lightweight": 8, "durability": 7, "traction": 9, "breathability": 8, "link": "https://www.adidas.com.cn/harden-vol-5-g55809"},
            # 力量内线型
            {"name": "Nike Air Force Max", "brand": "耐克/Nike", "price": 1099, "type": "力量内线型", "position": "大前锋,中锋", "court_type": "室内木地板", "foot_type": "正常脚型", "cushioning": 9, "support": 10, "lightweight": 6, "durability": 9, "traction": 9, "breathability": 7, "link": "https://www.nike.com/cn/t/air-force-max-basketball-shoes-5Q5z5r/CD4162-100"},
            {"name": "Adidas Pro Bounce 2019", "brand": "阿迪达斯/Adidas", "price": 899, "type": "力量内线型", "position": "大前锋,中锋", "court_type": "室内木地板", "foot_type": "正常脚型", "cushioning": 8, "support": 9, "lightweight": 6, "durability": 9, "traction": 8, "breathability": 7, "link": "https://www.adidas.com.cn/pro-bounce-2019-low-f36277"},
            {"name": "Li-Ning Way of Wade 8", "brand": "李宁", "price": 1299, "type": "力量内线型", "position": "大前锋,中锋", "court_type": "室内木地板", "foot_type": "正常脚型", "cushioning": 9, "support": 10, "lightweight": 7, "durability": 8, "traction": 9, "breathability": 8, "link": "https://lining.tmall.com/p/rd781245.htm"},
            {"name": "Nike LeBron 19", "brand": "耐克/Nike", "price": 1599, "type": "力量内线型", "position": "大前锋,中锋", "court_type": "室内木地板", "foot_type": "正常脚型", "cushioning": 10, "support": 10, "lightweight": 6, "durability": 9, "traction": 9, "breathability": 8, "link": "https://www.nike.com/cn/t/lebron-19-basketball-shoes-5T1K6m/DJ5423-100"},
            # 快速突破型
            {"name": "Nike Kyrie 7", "brand": "耐克/Nike", "price": 1099, "type": "快速突破型", "position": "控球后卫,得分后卫", "court_type": "室内木地板", "foot_type": "正常脚型", "cushioning": 8, "support": 8, "lightweight": 9, "durability": 7, "traction": 10, "breathability": 8, "link": "https://www.nike.com/cn/t/kyrie-7-basketball-shoes-3m44WX/CT1014-001"},
            {"name": "Adidas Dame 7", "brand": "阿迪达斯/Adidas", "price": 899, "type": "快速突破型", "position": "控球后卫,得分后卫", "court_type": "室内木地板", "foot_type": "正常脚型", "cushioning": 8, "support": 7, "lightweight": 9, "durability": 8, "traction": 9, "breathability": 8, "link": "https://www.adidas.com.cn/dame-7-g55107"},
            {"name": "Li-Ning Yu Shuai 14", "brand": "李宁", "price": 899, "type": "快速突破型", "position": "控球后卫,得分后卫", "court_type": "室内木地板", "foot_type": "正常脚型", "cushioning": 8, "support": 8, "lightweight": 9, "durability": 7, "traction": 9, "breathability": 8, "link": "https://lining.tmall.com/p/rd681245.htm"},
            # 精准投篮型
            {"name": "Nike Kobe 5 Protro", "brand": "耐克/Nike", "price": 1599, "type": "精准投篮型", "position": "得分后卫,小前锋", "court_type": "室内木地板", "foot_type": "正常脚型", "cushioning": 9, "support": 8, "lightweight": 8, "durability": 7, "traction": 10, "breathability": 8, "link": "https://www.nike.com/cn/t/kobe-5-protro-basketball-shoes-9mJ5fD/CD4991-101"},
            {"name": "Nike KD14", "brand": "耐克/Nike", "price": 1299, "type": "精准投篮型", "position": "得分后卫,小前锋", "court_type": "室内木地板", "foot_type": "正常脚型", "cushioning": 9, "support": 9, "lightweight": 8, "durability": 8, "traction": 9, "breathability": 8, "link": "https://www.nike.com/cn/t/kd14-basketball-shoes-m8nR4B/CW3935-100"},
            {"name": "Jordan Jumpman 2021", "brand": "乔丹/Air Jordan", "price": 1099, "type": "精准投篮型", "position": "得分后卫,小前锋", "court_type": "室内木地板", "foot_type": "正常脚型", "cushioning": 8, "support": 9, "lightweight": 8, "durability": 8, "traction": 9, "breathability": 8, "link": "https://www.nike.com/cn/t/jumpman-2021-basketball-shoes-6VqB4g/DA1897-100"}
        ]
    
    def _clear_screen(self):
        """清屏函数"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def _print_header(self):
        """打印程序头部"""
        header = """
        =======================================================
                        篮球鞋推荐系统
        =======================================================
        """
        print(header)
    
    def _get_input(self, prompt: str, required: bool = True, input_type: str = "str") -> Any:
        """获取用户输入，支持类型转换和必填验证"""
        while True:
            user_input = input(prompt).strip()
            
            if required and not user_input:
                print("该项为必填，请重新输入。")
                continue
            
            if not user_input:
                return None
            
            try:
                if input_type == "int":
                    return int(user_input)
                elif input_type == "float":
                    return float(user_input)
                else:
                    return user_input
            except ValueError:
                print(f"请输入有效的{input_type}类型数据。")
    
    def _get_choice(self, prompt: str, options: List[str], required: bool = True) -> str:
        """获取用户从选项中的选择"""
        while True:
            print(prompt)
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")
            
            choice = self._get_input("请输入选项编号: ", required)
            
            if not choice:
                return None
            
            try:
                choice_idx = int(choice) - 1
                if 0 <= choice_idx < len(options):
                    return options[choice_idx]
                else:
                    print(f"请输入1-{len(options)}之间的数字。")
            except ValueError:
                print("请输入有效的数字选项。")
    
    def _get_multiple_choices(self, prompt: str, options: List[str]) -> List[str]:
        """获取用户的多项选择"""
        selected = []
        print(prompt)
        print("请输入选项编号（多个选项用逗号分隔，输入0结束）:")
        
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        while True:
            choice_input = self._get_input("请输入: ", False)
            
            if not choice_input or choice_input == "0":
                break
            
            try:
                choices = [int(c.strip()) - 1 for c in choice_input.split(",")]
                valid_choices = [c for c in choices if 0 <= c < len(options)]
                
                for idx in valid_choices:
                    if options[idx] not in selected:
                        selected.append(options[idx])
                
                if len(valid_choices) < len(choices):
                    print("部分选项无效，已忽略。")
                
                print(f"已选择: {', '.join(selected)}")
            except ValueError:
                print("输入格式不正确，请使用逗号分隔选项编号。")
        
        return selected
    
    def collect_user_data(self):
        """收集用户数据"""
        self._clear_screen()
        self._print_header()
        print("请完成以下问卷，我们将为您推荐最适合的篮球鞋。\n")
        
        # 步骤1：基本信息
        print("===== 步骤1：基本信息 =====")
        self.user_data["height"] = self._get_input("您的身高（cm）: ", True, "int")
        self.user_data["weight"] = self._get_input("您的体重（kg）: ", True, "int")
        self.user_data["foot_type"] = self._get_choice(
            "您的脚型是: ",
            ["正常脚型", "高足弓", "扁平足", "宽脚掌"]
        )
        
        # 判断是否为篮球新手
        is_beginner = self._get_choice(
            "您是篮球新手吗？: ",
            ["是", "否"]
        )
        self.user_data["is_beginner"] = "true" if is_beginner == "是" else "false"
        
        print("\n感谢您完成基本信息填写！\n")
        time.sleep(1)
        self._clear_screen()
        self._print_header()
        
        # 步骤2：打球风格（根据是否新手显示不同问题）
        print("===== 步骤2：打球风格 =====")
        if self.user_data["is_beginner"] == "false":
            # 非新手问题
            self.user_data["playing_position"] = self._get_choice(
                "您在球场上主要担任的位置是: ",
                ["控球后卫", "得分后卫", "小前锋", "大前锋", "中锋"]
            )
            
            self.user_data["offensive_strength"] = self._get_choice(
                "您最擅长的进攻方式是: ",
                ["外线投篮（三分、中投）", "突破上篮/扣篮", "背身单打", "组织传球", "无球跑动和空切"]
            )
            
            self.user_data["defensive_strength"] = self._get_choice(
                "您最擅长的防守方式是: ",
                ["贴身防守和抢断", "盖帽和篮板", "团队防守和协防", "防守意识和预判", "全场紧逼"]
            )
        else:
            # 新手问题
            self.user_data["desired_position"] = self._get_choice(
                "您未来希望主要担任的位置是: ",
                ["控球后卫", "得分后卫", "小前锋", "大前锋", "中锋"]
            )
            
            self.user_data["admire_style"] = self._get_choice(
                "您最欣赏的打球风格是: ",
                ["快速突破和扣篮", "精准投篮", "出色的传球和组织", "强硬的防守", "全面均衡的表现"]
            )
        
        print("\n感谢您完成打球风格填写！\n")
        time.sleep(1)
        self._clear_screen()
        self._print_header()
        
        # 步骤3：球鞋偏好
        print("===== 步骤3：球鞋偏好 =====")
        self.user_data["court_type"] = self._get_choice(
            "您主要在什么场地打球？: ",
            ["室内木地板", "室外水泥地", "两者皆有"]
        )
        
        print("您的预算范围（元）:")
        self.user_data["price_min"] = self._get_input("最低预算（0表示无下限）: ", True, "int")
        self.user_data["price_max"] = self._get_input("最高预算（0表示无上限）: ", True, "int")
        
        self.user_data["shoe_features"] = self._get_multiple_choices(
            "请选择您最看重的球鞋特性（可多选）:",
            ["缓震性能", "支撑稳定性", "轻便灵活性", "耐磨耐用性", "抓地力", "透气性"]
        )
        
        self.user_data["shoe_brand"] = self._get_choice(
            "您有偏好的品牌吗？: ",
            ["耐克/Nike", "阿迪达斯/Adidas", "乔丹/Air Jordan", "安德玛/Under Armour", "匹克", "李宁", "安踏", "无所谓"],
            False
        )
        
        self.user_data["shoe_weight"] = self._get_choice(
            "您对球鞋重量的偏好是？: ",
            ["非常轻便", "中等重量", "偏厚重（更稳定）", "无所谓"],
            False
        )
        
        print("\n感谢您完成所有问卷！正在分析您的篮球风格...\n")
        time.sleep(2)
    
    def analyze_playing_style(self):
        """分析用户打球风格"""
        # 初始化风格得分
        style_scores = {
            "力量内线型": 0,
            "快速突破型": 0,
            "精准投篮型": 0,
            "全面均衡型": 0,
            "组织传球型": 0,
            "防守专家型": 0,
            "团队配合型": 0
        }
        
        if self.user_data["is_beginner"] == "false":
            # 非新手逻辑
            if "playing_position" in self.user_data:
                position = self.user_data["playing_position"]
                if position in ("大前锋", "中锋"):
                    style_scores["力量内线型"] += 30
                elif position == "控球后卫":
                    style_scores["组织传球型"] += 30
                    style_scores["快速突破型"] += 20
                elif position == "得分后卫":
                    style_scores["精准投篮型"] += 30
                    style_scores["快速突破型"] += 20
                elif position == "小前锋":
                    style_scores["全面均衡型"] += 30
            
            if "offensive_strength" in self.user_data:
                offense = self.user_data["offensive_strength"]
                if offense == "外线投篮（三分、中投）":
                    style_scores["精准投篮型"] += 25
                elif offense == "突破上篮/扣篮":
                    style_scores["快速突破型"] += 25
                    style_scores["力量内线型"] += 15
                elif offense == "背身单打":
                    style_scores["力量内线型"] += 25
                elif offense == "组织传球":
                    style_scores["组织传球型"] += 25
                elif offense == "无球跑动和空切":
                    style_scores["团队配合型"] += 25
            
            if "defensive_strength" in self.user_data:
                defense = self.user_data["defensive_strength"]
                if defense == "贴身防守和抢断":
                    style_scores["防守专家型"] += 20
                elif defense == "盖帽和篮板":
                    style_scores["力量内线型"] += 20
                elif defense == "团队防守和协防":
                    style_scores["团队配合型"] += 20
                elif defense == "防守意识和预判":
                    style_scores["防守专家型"] += 20
                elif defense == "全场紧逼":
                    style_scores["快速突破型"] += 20
        else:
            # 新手逻辑
            if "desired_position" in self.user_data:
                position = self.user_data["desired_position"]
                if position in ("大前锋", "中锋"):
                    style_scores["力量内线型"] += 30
                elif position == "控球后卫":
                    style_scores["组织传球型"] += 30
                    style_scores["快速突破型"] += 20
                elif position == "得分后卫":
                    style_scores["精准投篮型"] += 30
                    style_scores["快速突破型"] += 20
                elif position == "小前锋":
                    style_scores["全面均衡型"] += 30
            
            if "admire_style" in self.user_data:
                admire = self.user_data["admire_style"]
                if admire == "快速突破和扣篮":
                    style_scores["快速突破型"] += 25
                    style_scores["力量内线型"] += 15
                elif admire == "精准投篮":
                    style_scores["精准投篮型"] += 25
                elif admire == "出色的传球和组织":
                    style_scores["组织传球型"] += 25
                elif admire == "强硬的防守":
                    style_scores["防守专家型"] += 25
                elif admire == "全面均衡的表现":
                    style_scores["全面均衡型"] += 25
        
        # 根据身体数据调整风格得分
        if "height" in self.user_data and "weight" in self.user_data:
            height = self.user_data["height"]
            weight = self.user_data["weight"]
            
            if height > 190 and weight > 85:
                style_scores["力量内线型"] += 20
            elif height < 180 and weight < 75:
                style_scores["快速突破型"] += 15
                style_scores["组织传球型"] += 15
            else:
                style_scores["全面均衡型"] += 15
        
        # 找出最高分的风格
        highest_score = 0
        primary_style = ""
        
        for style, score in style_scores.items():
            if score > highest_score:
                highest_score = score
                primary_style = style
        
        # 保存风格分析结果
        self.style_analysis = {
            "primary_style": primary_style,
            "style_scores": style_scores
        }
        
        # 显示风格分析结果
        self._clear_screen()
        self._print_header()
        print("===== 您的篮球风格分析结果 =====\n")
        print(f"🏀 您的主要打球风格：{primary_style}")
        
        print("\n风格匹配度详情：")
        for style, score in style_scores.items():
            percentage = min(100, round(score * 0.8))
            bar = "█" * (percentage // 5)
            print(f"{style}: {percentage}% [{bar:<20}]")
        
        print("\n正在为您推荐最适合的篮球鞋...\n")
        time.sleep(2)
    
    def find_matching_shoes(self):
        """查找匹配的篮球鞋"""
        if not self.style_analysis:
            self.analyze_playing_style()
        
        primary_style = self.style_analysis["primary_style"]
        
        # 过滤球鞋
        matching_shoes = []
        
        for shoe in self.shoes_data:
            match_score = 0
            
            # 风格匹配
            if shoe["type"] == primary_style:
                match_score += 40
            elif shoe["type"] == "全面均衡型":
                match_score += 20
            
            # 场地类型匹配
            if "court_type" in self.user_data and self.user_data["court_type"]:
                if shoe["court_type"] == self.user_data["court_type"]:
                    match_score += 15
                elif self.user_data["court_type"] == "两者皆有":
                    match_score += 10
            
            # 品牌匹配
            if "shoe_brand" in self.user_data and self.user_data["shoe_brand"] and self.user_data["shoe_brand"] != "无所谓":
                brand_name = self.user_data["shoe_brand"].split("/")[0]
                if brand_name in shoe["brand"]:
                    match_score += 15
            
            # 重量偏好匹配
            if "shoe_weight" in self.user_data and self.user_data["shoe_weight"] and self.user_data["shoe_weight"] != "无所谓":
                if self.user_data["shoe_weight"] == "非常轻便" and shoe["lightweight"] >= 8:
                    match_score += 10
                elif self.user_data["shoe_weight"] == "中等重量" and 6 <= shoe["lightweight"] <= 8:
                    match_score += 10
                elif self.user_data["shoe_weight"] == "偏厚重（更稳定）" and shoe["lightweight"] <= 6:
                    match_score += 10
            
            # 价格范围
            if "price_min" in self.user_data and "price_max" in self.user_data:
                min_price = self.user_data["price_min"]
                max_price = self.user_data["price_max"]
                
                if min_price == 0 and max_price == 0:
                    match_score += 10
                elif min_price <= shoe["price"] <= max_price:
                    match_score += 10
            
            # 球鞋特性匹配
            if "shoe_features" in self.user_data and self.user_data["shoe_features"]:
                for feature in self.user_data["shoe_features"]:
                    if feature == "缓震性能" and shoe["cushioning"] >= 8:
                        match_score += 5
                    elif feature == "支撑稳定性" and shoe["support"] >= 8:
                        match_score += 5
                    elif feature == "轻便灵活性" and shoe["lightweight"] >= 8:
                        match_score += 5
                    elif feature == "耐磨耐用性" and shoe["durability"] >= 8:
                        match_score += 5
                    elif feature == "抓地力" and shoe["traction"] >= 8:
                        match_score += 5
                    elif feature == "透气性" and shoe["breathability"] >= 8:
                        match_score += 5
            
            # 添加到匹配列表
            if match_score >= 50:
                shoe_with_score = shoe.copy()
                shoe_with_score["match_score"] = match_score
                matching_shoes.append(shoe_with_score)
        
        # 按匹配度和相关性排序
        matching_shoes.sort(key=lambda x: (x["type"] == primary_style, x["match_score"]), reverse=True)
        
        # 最多返回12双鞋
        self.recommendations = matching_shoes[:12]
    
    def display_recommendations(self):
        """显示推荐结果"""
        if not self.recommendations:
            self.find_matching_shoes()
        
        self._clear_screen()
        self._print_header()
        
        if not self.recommendations:
            print("===== 推荐结果 =====\n")
            print("😔 抱歉，没有找到完全匹配您需求的篮球鞋。")
            print("以下是一些热销的篮球鞋，供您参考：\n")
            # 显示默认推荐
            default_shoes = self.shoes_data[:6]
            for i, shoe in enumerate(default_shoes, 1):
                self._print_shoe_info(i, shoe)
        else:
            print("===== 为您推荐的篮球鞋 =====\n")
            print(f"根据您的打球风格 ({self.style_analysis['primary_style']}) 和偏好，我们为您精选了以下篮球鞋：\n")
            
            for i, shoe in enumerate(self.recommendations, 1):
                self._print_shoe_info(i, shoe)
        
        print("\n价格仅供参考，实际购买时请以官方渠道为准。")
        print("在二级市场购买通常更经济实惠。\n")
    
    def _print_shoe_info(self, index: int, shoe: Dict[str, Any]):
        """打印单双鞋的信息"""
        print(f"{index}. {shoe['name']}")
        print(f"   品牌: {shoe['brand']}")
        print(f"   价格: ¥{shoe['price']}")
        print(f"   类型: {shoe['type']}")
        print(f"   适用位置: {shoe['position']}")
        print(f"   适用场地: {shoe['court_type']}")
        
        # 打印特性评分
        print("   特性评分:")
        print(f"     缓震性能: {'★' * shoe['cushioning']}{'☆' * (10 - shoe['cushioning'])}")
        print(f"     支撑稳定: {'★' * shoe['support']}{'☆' * (10 - shoe['support'])}")
        print(f"     轻便灵活: {'★' * shoe['lightweight']}{'☆' * (10 - shoe['lightweight'])}")
        print(f"     耐磨耐用: {'★' * shoe['durability']}{'☆' * (10 - shoe['durability'])}")
        print(f"     抓地性能: {'★' * shoe['traction']}{'☆' * (10 - shoe['traction'])}")
        print(f"     透气性能: {'★' * shoe['breathability']}{'☆' * (10 - shoe['breathability'])}")
        
        print(f"   购买链接: {shoe['link']}")
        print()
    
    def run(self):
        """运行推荐系统"""
        try:
            # 收集用户数据
            self.collect_user_data()
            
            # 分析打球风格
            self.analyze_playing_style()
            
            # 查找匹配的球鞋
            self.find_matching_shoes()
            
            # 显示推荐结果
            self.display_recommendations()
            
            # 询问用户是否重新开始
            while True:
                restart = self._get_choice("是否重新进行测评？", ["是", "否"])
                if restart == "是":
                    # 重置数据
                    self.user_data = {}
                    self.style_analysis = {}
                    self.recommendations = []
                    self.run()
                    break
                else:
                    print("\n感谢使用篮球鞋推荐系统！祝您球技大涨！🏀")
                    break
        except KeyboardInterrupt:
            print("\n\n程序已中断，感谢使用！")
        except Exception as e:
            print(f"\n程序发生错误: {e}")
            print("请联系管理员或重新运行程序。")

if __name__ == "__main__":
    recommender = BasketballShoeRecommender()
    recommender.run()