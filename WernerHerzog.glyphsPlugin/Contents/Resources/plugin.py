import objc

from GlyphsApp import Glyphs, DOCUMENTCLOSED
from GlyphsApp.plugins import GeneralPlugin


class WernerHerzog(GeneralPlugin):

    @objc.python_method
    def saveCallback(self, notification):
        q = [
            # "Chance is the lifeblood of cinema.",
            "A badge of honour is to fail a film theory class.",
            "Ask for forgiveness, not permission.",
            "Day one is the point of no return",
            "Develop your own voice.",
            "Don’t be fearful of rejection.",
            "Emoji? Let them keep smiling. I don't care.",
            "Every man should pull a boat over a mountain once in his life.",
            "Expand your knowledge and understanding of music and literature, old and modern.",
            "For me, the best description of hunger is the description of bread.",
            "Get used to the bear behind you.",
            "Guerilla tactics are best.",
            "If you do not have an absolutely clear vision of something, where you can follow the light to the end of the tunnel, then it doesn't matter whether you're bold or cowardly, or whether you're stupid or intelligent. Doesn't get you anywhere.",
            "Ignite the fire withing and explore unknown territory.",
            "I cannot work fast enough. I cannot cope fast enough, really. And just releasing a film is hard.",
            "I don't spend sleepless nights over getting very bad reviews.",
            "Learn to live with your mistakes.",
            "Life on our planet has been a constant series of cataclysmic events, and we are more suitable for extinction than a trilobite or a reptile. So we will vanish. There's no doubt in my heart.",
            "Manoeuvre and mislead, but always deliver.",
            "Never wallow in your troubles; despair must be kept private and brief.",
            "Send out all your dogs and one might return with prey.",
            "There is never and excuse not to finish a film.",
            "The universe is monstrously indifferent to the presence of man.",
            "The universe is not harmonious: you know that by looking outside.",
            "Thwart institutional cowardice.",
            "Walk straight ahead, never detour.",
            "We ought to be grateful that the Universe out there knows no smile.",
            "Yes, the pyramids have been built, but if you give me 300,000 disciplined men and give me 30 years, I could build a bigger one.",
            "You are all wrong.",
        ]
        try:
            from random import choice
            Glyphs.showNotification("Werner Herzog says", choice(q))
        except:
            import traceback
            print(traceback.format_exc())

    @objc.python_method
    def start(self):
        Glyphs.addCallback(self.saveCallback, DOCUMENTCLOSED)
