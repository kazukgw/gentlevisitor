import datetime

import gentlevisitor as genvis


def init_schedule():
    return {
        'start_time': datetime.time(12, 27, 00),
        'end_time': datetime.time(13, 58, 00),
        'every': 3,
        'active_weekday': '*',
    }


def init_dbparams():
    return genvis.dbutil.Params(
        'crawler_wikipedia',
        'mysql',
        '3306',
        'crawler',
        'crawler',
        None
    )


def init_proxies():
    return [
        # {
        #     'http': 'http://10.10.1.10:3128',
        #     'https': 'http://10.10.1.10:1080',
        # },
    ]


class Controller(genvis.ControllerBase):

    def can_run(self, ctx, bot):
        return True

    def on_fetch(self, sess, bot):
        sess.state = 200
        sess.result = 200
        bot.session_repo.save(sess)

    def on_except(self, e, sess, bot):
        pass


def main():

    b = genvis.Bot(init_schedule(), init_proxies(),
                   Controller(), init_dbparams())
    b.start()


if __name__ == '__main__':
    main()
