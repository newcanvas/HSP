def MassVote(N: int, Votes: list) -> str:
    for i in range(N):
        if Votes.count(max(Votes)) > 1:
            return "no winner"

        if max(Votes) / sum(Votes) > 0.5:
            return f"majority winner {Votes.index(max(Votes)) + 1}"

        return f"minority winner {Votes.index(max(Votes)) + 1}"

