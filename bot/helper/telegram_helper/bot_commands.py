#!/usr/bin/env python3
from bot import CMD_SUFFIX, config_dict

class _BotCommands:
    def __init__(self):
        self.StartCommand = 'start'
        self.MirrorCommand = [f'mirror1{CMD_SUFFIX}', f'm1{CMD_SUFFIX}']
        self.QbMirrorCommand = [f'qbmirror1{CMD_SUFFIX}', f'qm1{CMD_SUFFIX}']
        self.YtdlCommand = [f'ytdl1{CMD_SUFFIX}', f'y1{CMD_SUFFIX}']
        self.LeechCommand = [f'leech1{CMD_SUFFIX}', f'l1{CMD_SUFFIX}']
        self.QbLeechCommand = [f'qbleech1{CMD_SUFFIX}', f'ql1{CMD_SUFFIX}']
        self.YtdlLeechCommand = [f'ytdlleech1{CMD_SUFFIX}', f'yl1{CMD_SUFFIX}']
        if config_dict['SHOW_EXTRA_CMDS']:
            self.MirrorCommand.extend([f'unzipmirror1{CMD_SUFFIX}', f'uzm1{CMD_SUFFIX}', f'zipmirror{CMD_SUFFIX}', f'zm{CMD_SUFFIX}'])
            self.QbMirrorCommand.extend([f'qbunzipmirror1{CMD_SUFFIX}', f'quzm1{CMD_SUFFIX}', f'qbzipmirror{CMD_SUFFIX}', f'qzm{CMD_SUFFIX}'])
            self.YtdlCommand.extend([f'ytdlzip1{CMD_SUFFIX}', f'yz1{CMD_SUFFIX}'])
            self.LeechCommand.extend([f'unzipleech1{CMD_SUFFIX}', f'uzl1{CMD_SUFFIX}', f'zipleech{CMD_SUFFIX}', f'zl{CMD_SUFFIX}'])
            self.QbLeechCommand.extend([f'qbunzipleech1{CMD_SUFFIX}', f'quzl1{CMD_SUFFIX}', f'qbzipleech{CMD_SUFFIX}', f'qzl{CMD_SUFFIX}'])
            self.YtdlLeechCommand.extend([f'ytdlzipleech1{CMD_SUFFIX}', f'yzl1{CMD_SUFFIX}'])
        self.CloneCommand = [f'clone1{CMD_SUFFIX}', f'c1{CMD_SUFFIX}']
        self.CountCommand = f'count1{CMD_SUFFIX}'
        self.DeleteCommand = f'del1{CMD_SUFFIX}'
        self.CancelMirror = f'cancel1{CMD_SUFFIX}'
        self.CancelAllCommand = [f'cancelall{CMD_SUFFIX}', 'cancellallbot']
        self.ListCommand = f'list1{CMD_SUFFIX}'
        self.SearchCommand = f'search1{CMD_SUFFIX}'
        self.StatusCommand = [f'status1{CMD_SUFFIX}', f's{CMD_SUFFIX}', 'statusall']
        self.UsersCommand = f'users1{CMD_SUFFIX}'
        self.AuthorizeCommand = [f'authorize1{CMD_SUFFIX}', f'a{CMD_SUFFIX}']
        self.UnAuthorizeCommand = [f'unauthorize1{CMD_SUFFIX}', f'ua{CMD_SUFFIX}']
        self.AddBlackListCommand = [f'blacklist1{CMD_SUFFIX}', f'bl{CMD_SUFFIX}']
        self.RmBlackListCommand = [f'rmblacklist1{CMD_SUFFIX}', f'rbl{CMD_SUFFIX}']
        self.AddSudoCommand = f'addsudo1{CMD_SUFFIX}'
        self.RmSudoCommand = f'rmsudo1{CMD_SUFFIX}'
        self.PingCommand = [f'ping1{CMD_SUFFIX}', f'p1{CMD_SUFFIX}']
        self.RestartCommand = [f'restart1{CMD_SUFFIX}', f'r1{CMD_SUFFIX}', 'restartall']
        self.StatsCommand = [f'stats1{CMD_SUFFIX}', f'st1{CMD_SUFFIX}']
        self.HelpCommand = f'help1{CMD_SUFFIX}'
        self.LogCommand = f'log1{CMD_SUFFIX}'
        self.ShellCommand = f'shell{CMD_SUFFIX}'
        self.EvalCommand = f'eval{CMD_SUFFIX}'
        self.ExecCommand = f'exec{CMD_SUFFIX}'
        self.ClearLocalsCommand = f'clearlocals{CMD_SUFFIX}'
        self.BotSetCommand = [f'bsetting1{CMD_SUFFIX}', f'bs1{CMD_SUFFIX}']
        self.UserSetCommand = [f'usetting1{CMD_SUFFIX}', f'us1{CMD_SUFFIX}']
        self.BtSelectCommand = f'btsel1{CMD_SUFFIX}'
        self.CategorySelect = f'ctsel1{CMD_SUFFIX}'
        self.SpeedCommand = [f'speedtest1{CMD_SUFFIX}', f'sp1{CMD_SUFFIX}']
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
