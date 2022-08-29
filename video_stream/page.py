import Famcy
class videoStreamPage(Famcy.FamcyPage):
    def __init__(self):
        super(videoStreamPage, self).__init__()

        self.card_0 = self.card0()
        self.layout.addWidget(self.card_0, 0, 0)

    def card0(self):
        _card = Famcy.FamcyCard()

        _v = nodejs_video()

        _card.layout.addWidget(_v, 0, 0)

        return _card

videoStreamPage.register("/video_stream", Famcy.ClassicStyle(), permission_level=0, background_thread=False, event_source_flag=True)


class nodejs_video(Famcy.FamcyBlock):
    def __init__(self, **kwargs):
        self.value = nodejs_video.generate_template_content()
        super(nodejs_video, self).__init__(**kwargs)
        self.init_block()

    @classmethod
    def generate_template_content(cls, fblock_type=None):
        return {}

    def init_block(self):
        self.body = Famcy.div()
        self.body["id"] = self.id

        _c = Famcy.canvas()
        _c["id"] = "video-canvas"+self.id

        _sjs = Famcy.script()
        _sjs["src"] = "asset/js/jsmpeg.min.js"

        _s = Famcy.script()
        _s.innerHTML = '''
        var canvas = document.getElementById('video-canvas%s');
        var url = 'ws://'+document.location.hostname+':8082/';
        var player = new JSMpeg.Player(url, {canvas: canvas});
        ''' % (self.id)

        self.body.addElement(_c)
        self.body.addElement(_sjs)
        self.body.addElement(_s)

    def render_inner(self):
        return self.body