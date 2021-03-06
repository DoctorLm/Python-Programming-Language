'''
    作业涉及的代码和文档，请以附件的形式上传。
    本次作业算作附加题，会在大作业1的基础上适当调整分数（不做该作业也不会有惩罚）。
    
    依照学术诚信条款，我保证此回答为本人原创，所有回答中引用的外部材料已经做了出处标记。
    1（1分）
    本次实验为强化学习任务，使用深度神经网络学习俄罗斯方块游戏的策略。该游戏涉及5种动作：空操作、向左移动、向右移动、旋转和下落。游戏代码已在附件中给出，相应的调用方式如下：
    import sys
    sys.path.append("game/")
    import dummy_game
    import tetris_fun as game
    
    #开启游戏模拟器
    game_state = game.GameState()
    
    #执行动作，与模拟器交互获得奖励和下一帧图像以及游戏是否终止
    img_state, reward, terminal = game_state.frame_step(action)
    
    #游戏分数
    game_state.score
    
    作业要求：
    撰写实验报告，介绍超参数的设置、网络结构的设计及训练的结果分析。
    提交实验代码、实验报告以及训练后的网络参数文件。
    所需环境参考单元8
    
    
    game.rar下载
'''

