

class ChessCoordinate:
    _interned = dict()

    def __new__(cls, file, rank):
        if len(file) != 1:
            raise ValueError(
                f"{cls.__name__} file can only "
                f"have a length of 1, not {len(file)}"
            )
        if file not in "abcdefgh":
            raise ValueError(
                f"{cls.__name__} file {file!r} is out of range."
            )
        if rank not in range(1, 9):
            raise ValueError(
                f"{cls.__name__} rank {rank!r} is out of range."
            )

        key = (file, rank)
        if key not in cls._interned:
            obj = super().__new__(cls)
            obj._file, obj._rank = file, rank
            cls._interned[key] = obj
        return cls._interned.get(key)

    @property
    def file(self):
        return self._file

    @property
    def rank(self):
        return self._rank

    def __repr__(self):
        fields = (
            f"{k.lstrip('_')}={v}" for k, v in sorted(vars(self).items())
        )
        return f"{type(self).__name__}({', '.join(fields)})"

    def __str__(self):
        return f"{self.file}~{self.rank}"


if __name__ == '__main__':
    white_queen = ChessCoordinate('d', 4)
    print(white_queen)
    pass

