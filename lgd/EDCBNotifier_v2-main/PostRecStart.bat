@echo off
chcp 932 > nul

rem // �E�C���h�E���\���ɂ���
rem _EDCBX_HIDE_

rem // �p�����[�^�����ϐ��ɓn��
rem // �������邱�Ƃ� Python ���ł����ϐ����Q�Ƃł���
rem _EDCBX_DIRECT_

rem // �����\��Ȃ�I��
if "%RecMode%" == "4" (
    goto :eof
)

rem // Python �ɓ�����

python %~dp0\EDCBNotifier\EDCBNotifier.py PostRecStart
exit
