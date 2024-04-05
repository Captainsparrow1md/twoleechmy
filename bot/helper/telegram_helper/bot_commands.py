#!/usr/bin/env python3
from bot import CMD_SUFFIX, config_dict

class _BotCommands:
    def __init__(self):
        self.StartCommand = 'start'
        self.MirrorCommand = [f'mirror4{CMD_SUFFIX}', f'm4{CMD_SUFFIX}']
        self.QbMirrorCommand = [f'qbmirror4{CMD_SUFFIX}', f'qm4{CMD_SUFFIX}']
        self.YtdlCommand = [f'ytdl4{CMD_SUFFIX}', f'y4{CMD_SUFFIX}']
        self.LeechCommand = [f'leech4{CMD_SUFFIX}', f'l4{CMD_SUFFIX}']
        self.QbLeechCommand = [f'qbleech4{CMD_SUFFIX}', f'ql4{CMD_SUFFIX}']
        self.YtdlLeechCommand = [f'ytdlleech4{CMD_SUFFIX}', f'yl4{CMD_SUFFIX}']
        if config_dict['SHOW_EXTRA_CMDS']:
            self.MirrorCommand.extend([f'unzipmirror4{CMD_SUFFIX}', f'uzm4{CMD_SUFFIX}', f'zipmirror4{CMD_SUFFIX}', f'zm4{CMD_SUFFIX}'])
            self.QbMirrorCommand.extend([f'qbunzipmirror4{CMD_SUFFIX}', f'quzm4{CMD_SUFFIX}', f'qbzipmirror4{CMD_SUFFIX}', f'qzm4{CMD_SUFFIX}'])
            self.YtdlCommand.extend([f'ytdlzip4{CMD_SUFFIX}', f'yz4{CMD_SUFFIX}'])
            self.LeechCommand.extend([f'unzipleech4{CMD_SUFFIX}', f'uzl4{CMD_SUFFIX}', f'zipleech4{CMD_SUFFIX}', f'zl4{CMD_SUFFIX}'])
            self.QbLeechCommand.extend([f'qbunzipleech4{CMD_SUFFIX}', f'quzl4{CMD_SUFFIX}', f'qbzipleech4{CMD_SUFFIX}', f'qzl4{CMD_SUFFIX}'])
            self.YtdlLeechCommand.extend([f'ytdlzipleech4{CMD_SUFFIX}', f'yzl4{CMD_SUFFIX}'])
        self.CloneCommand = [f'clone4{CMD_SUFFIX}', f'c4{CMD_SUFFIX}']
        self.CountCommand = f'count4{CMD_SUFFIX}'
        self.DeleteCommand = f'del4{CMD_SUFFIX}'
        self.CancelMirror = f'cancel4{CMD_SUFFIX}'
        self.CancelAllCommand = [f'cancelall{CMD_SUFFIX}', 'cancellallbot']
        self.ListCommand = f'list4{CMD_SUFFIX}'
        self.SearchCommand = f'search4{CMD_SUFFIX}'
        self.StatusCommand = [f'status4{CMD_SUFFIX}', f's4{CMD_SUFFIX}', 'statusall']
        self.UsersCommand = f'users4{CMD_SUFFIX}'
        self.AuthorizeCommand = [f'authorize{CMD_SUFFIX}', f'a{CMD_SUFFIX}']
        self.UnAuthorizeCommand = [f'unauthorize{CMD_SUFFIX}', f'ua{CMD_SUFFIX}']
        self.AddBlackListCommand = [f'blacklist , {CMD_SUFFIX}', f'bl{CMD_SUFFIX}']
        self.RmBlackListCommand = [f'rmblacklist{CMD_SUFFIX}', f'rbl{CMD_SUFFIX}']
        self.AddSudoCommand = f'addsudo{CMD_SUFFIX}'
        self.RmSudoCommand = f'rmsudo{CMD_SUFFIX}'
        self.PingCommand = [f'ping4{CMD_SUFFIX}', f'p4{CMD_SUFFIX}']
        self.RestartCommand = [f'restart4{CMD_SUFFIX}', f'r4{CMD_SUFFIX}', 'restartall']
        self.StatsCommand = [f'stats4{CMD_SUFFIX}', f'st4{CMD_SUFFIX}']
        self.HelpCommand = f'help4{CMD_SUFFIX}'
        self.LogCommand = f'log4{CMD_SUFFIX}'
        self.ShellCommand = f'shell{CMD_SUFFIX}'
        self.EvalCommand = f'eval{CMD_SUFFIX}'
        self.ExecCommand = f'exec{CMD_SUFFIX}'
        self.ClearLocalsCommand = f'clearlocals{CMD_SUFFIX}'
        self.BotSetCommand = [f'bsetting4{CMD_SUFFIX}', f'bs4{CMD_SUFFIX}']
        self.UserSetCommand = [f'usetting4{CMD_SUFFIX}', f'us4{CMD_SUFFIX}']
        self.BtSelectCommand = f'btsel4{CMD_SUFFIX}'
        self.CategorySelect = f'ctsel4{CMD_SUFFIX}'
        self.SpeedCommand = [f'speedtest4{CMD_SUFFIX}', f'sp4{CMD_SUFFIX}']
        self.RssCommand = f'rss{CMD_SUFFIX}'
        self.LoginCommand = 'login'
        self.AddImageCommand = f'addimg{CMD_SUFFIX}'
        self.ImagesCommand = f'images{CMD_SUFFIX}'
        self.IMDBCommand = f'imdb{CMD_SUFFIX}'
        self.AniListCommand = f'anime{CMD_SUFFIX}'
        self.AnimeHelpCommand = f'animehelp{CMD_SUFFIX}'
        self.MediaInfoCommand = [f'mediainfo{CMD_SUFFIX}', f'mi{CMD_SUFFIX}']
        self.MyDramaListCommand = f'mdl{CMD_SUFFIX}'
        self.GDCleanCommand = [f'gdclean{CMD_SUFFIX}', f'gc{CMD_SUFFIX}']
        self.BroadcastCommand = [f'broadcast{CMD_SUFFIX}', f'bc{CMD_SUFFIX}']

BotCommands = _BotCommands()
