#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
�������ߣ�̷��
"""
import random
# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����
def name_to_number(cboice_name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if cboice_name=="ʯͷ":
	    return 0
    elif cboice_name=="ʷ����": 
	    return 1
    elif cboice_name=="��":
	    return 2
    elif cboice_name=="����":
	    return 3
    elif cboice_name=="����":
	    return 4
    else:
        return 5    
    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��
def number_to_name(comp_number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if comp_number==0:
      return "ʯͷ"
    elif comp_number==1:
      return "ʷ����"
    elif comp_number==2:
      return "��"
    elif comp_number==3:
      return "����"
    elif comp_number==4:
      return "����"
    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��
def rpsls(cboice_name):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
    """
    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice
    player_cboice=name_to_number(cboice_name)
    if player_cboice==5:
      print("Error: No Correct Name")
    else:
      print("����ѡ��Ϊ��%s"%(cboice_name))
    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
      comp_number=random.randint(0,4)
    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number
      player_cboice_number=number_to_name(comp_number)	
    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
      print("������ѡ��Ϊ��%s"%(player_cboice_number))
    # ����Ļ����ʾ�����ѡ����������
      rule=comp_number-player_cboice 
      if rule==2 or rule==-3 or rule==1 or rule==-4:
        print("����Ӯ��")
      elif rule==0:
        print("�����������һ����")
      else:
       print("��Ӯ��")  
    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�
# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��
# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
cboice_name=input()
rpsls(cboice_name)
