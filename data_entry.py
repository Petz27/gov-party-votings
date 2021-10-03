# class for processing Data from https://www.parlament.gv.at/PAKT/RGES/

class DataEntry:
    def __init__(self):
        self.disagreeing_parties = []
    title = ""
    pub_date = ""
    link = ""
    info = ""
    v_vote = False
    s_vote = False
    g_vote = False
    n_vote = False
    f_vote = False

    def print_entry(self):
        print(f'{self.title} vom {self.pub_date}')
        print(self.info)
        print(self.link)

    def set_all_votes_true(self):
        self.v_vote = True
        self.s_vote = True
        self.g_vote = True
        self.n_vote = True
        self.f_vote = True

    def print_disagreeing_parties(self):
        print(self.disagreeing_parties)

    def process_info(self):
        if self.info:
            self.set_all_votes_true()
            new_info = self.info.split("dagegen:", 1)[1]
            if 'V' in new_info:
                self.v_vote = False
                self.disagreeing_parties.append('V')
            if 'S' in new_info:
                self.s_vote = False
                self.disagreeing_parties.append('S')
            if 'G' in new_info:
                self.g_vote = False
                self.disagreeing_parties.append('G')
            if 'N' in new_info:
                self.n_vote = False
                self.disagreeing_parties.append('N')
            if 'F' in new_info:
                self.f_vote = False
                self.disagreeing_parties.append('F')
