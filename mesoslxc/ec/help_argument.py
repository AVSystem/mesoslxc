from mesoslxc.ec.argument import Argument


class HelpArgument(Argument):
    def do(self):
        print("""
            help:

                Argument    < STDIN proto               > STDOUT proto

                launch      < containerizer::Launch
                update      < containerizer::Update
                usage       < containerizer::Usage      > mesos::ResourceStatistics
                wait        < containerizer::Wait       > containerizer::Termination
                destroy     < containerizer::Destroy
                containers                              > containerizer::Containers
                recover
                help
            """)
