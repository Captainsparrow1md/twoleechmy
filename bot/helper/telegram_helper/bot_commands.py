#!/usr/bin/env python3
from bot import CMD_SUFFIX, config_dict

class _BotCommands:
    def __init__(self):
        self.StartCommand = 'start'
        self.MirrorCommand = [f'mirror3{CMD_SUFFIX}', f'm3{CMD_SUFFIX}']
        self.QbMirrorCommand = [f'qbmirror3{CMD_SUFFIX}', f'qm3{CMD_SUFFIX}']
        self.YtdlCommand = [f'ytdl3{CMD_SUFFIX}', f'y3{CMD_SUFFIX}']
        self.LeechCommand = [f'leech3{CMD_SUFFIX}', f'l3{CMD_SUFFIX}']
        self.QbLeechCommand = [f'qbleech3{CMD_SUFFIX}', f'ql3{CMD_SUFFIX}']
        self.YtdlLeechCommand = [f'ytdlleech3{CMD_SUFFIX}', f'yl3{CMD_SUFFIX}']
        if config_dict['SHOW_EXTRA_CMDS']:
            self.MirrorCommand.extend([f'unzipmirror3{CMD_SUFFIX}', f'uzm3{CMD_SUFFIX}', f'zipmirror3{CMD_SUFFIX}', f'zm3{CMD_SUFFIX}'])
            self.QbMirrorCommand.extend([f'qbunzipmirror3{CMD_SUFFIX}', f'quzm3{CMD_SUFFIX}', f'qbzipmirror3{CMD_SUFFIX}', f'qzm3{CMD_SUFFIX}'])
            self.YtdlCommand.extend([f'ytdlzip3{CMD_SUFFIX}', f'yz3{CMD_SUFFIX}'])
            self.LeechCommand.extend([f'unzipleech3{CMD_SUFFIX}', f'uzl3{CMD_SUFFIX}', f'zipleech3{CMD_SUFFIX}', f'zl3{CMD_SUFFIX}'])
            self.QbLeechCommand.extend([f'qbunzipleech3{CMD_SUFFIX}', f'quzl3{CMD_SUFFIX}', f'qbzipleech3{CMD_SUFFIX}', f'qzl3{CMD_SUFFIX}'])
            self.YtdlLeechCommand.extend([f'ytdlzipleech3{CMD_SUFFIX}', f'yzl3{CMD_SUFFIX}'])
        self.CloneCommand = [f'clone3{CMD_SUFFIX}', f'c3{CMD_SUFFIX}']
        self.CountCommand = f'count3{CMD_SUFFIX}'
        self.DeleteCommand = f'del3{CMD_SUFFIX}'
        self.CancelMirror = f'cancel3{CMD_SUFFIX}'
        self.CancelAllCommand = [f'cancelall{CMD_SUFFIX}', 'cancellallbot']
        self.ListCommand = f'list3{CMD_SUFFIX}'
        self.SearchCommand = f'search{CMD_SUFFIX}'
        self.StatusCommand = [f'status3{CMD_SUFFIX}', f's{CMD_SUFFIX}', 'statusall']
        self.UsersCommand = f'users{CMD_SUFFIX}'
        self.AuthorizeCommand = [f'authorize{CMD_SUFFIX}', f'a{CMD_SUFFIX}']
        self.UnAuthorizeCommand = [f'unauthorize{CMD_SUFFIX}', f'ua{CMD_SUFFIX}']
        self.AddBlackListCommand = [f'blacklist{CMD_SUFFIX}', f'bl{CMD_SUFFIX}']
        self.RmBlackListCommand = [f'rmblacklist{CMD_SUFFIX}', f'rbl{CMD_SUFFIX}']
        self.AddSudoCommand = f'addsudo{CMD_SUFFIX}'
        self.RmSudoCommand = f'rmsudo{CMD_SUFFIX}'
        self.PingCommand = [f'ping{CMD_SUFFIX}', f'p{CMD_SUFFIX}']
        self.RestartCommand = [f'restart3{CMD_SUFFIX}', f'r3{CMD_SUFFIX}', 'restartall']
        self.StatsCommand = [f'stats3{CMD_SUFFIX}', f'st3{CMD_SUFFIX}']
        self.HelpCommand = f'help{CMD_SUFFIX}'
        self.LogCommand = f'log3{CMD_SUFFIX}'
        self.ShellCommand = f'shell{CMD_SUFFIX}'
        self.EvalCommand = f'eval{CMD_SUFFIX}'
        self.ExecCommand = f'exec{CMD_SUFFIX}'
        self.ClearLocalsCommand = f'clearlocals2{CMD_SUFFIX}'
        self.BotSetCommand = [f'bsetting3{CMD_SUFFIX}', f'bs3{CMD_SUFFIX}']
        self.UserSetCommand = [f'usetting3{CMD_SUFFIX}', f'us3{CMD_SUFFIX}']
        self.BtSelectCommand = f'btsel3{CMD_SUFFIX}'
        self.CategorySelect = f'ctsel3{CMD_SUFFIX}'
        self.SpeedCommand = [f'speedtest3{CMD_SUFFIX}', f'sp3{CMD_SUFFIX}']
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
