import abc
import typing


class DataProcessor(abc.ABC):

    def __init__(self) -> None:
        self._storage: list[str] = []
        self._rank: int = 0
        self._total: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No data available in processor")
        rank: int = self._total - len(self._storage)
        value: str = self._storage.pop(0)
        return (rank, value)

    def get_total(self) -> int:
        return self._total

    def get_remaining(self) -> int:
        return len(self._storage)

    def get_name(self) -> str:
        return self.__class__.__name__


class NumericProcessor(DataProcessor):

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return bool(data) and all(
                isinstance(item, (int, float)) for item in data
            )
        return False

    def ingest(
        self,
        data: typing.Union[int, float, list[typing.Union[int, float]]]
    ) -> None:
        if not self.validate(data):
            raise TypeError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._storage.append(str(item))
                self._rank += 1
                self._total += 1
        else:
            self._storage.append(str(data))
            self._rank += 1
            self._total += 1


class TextProcessor(DataProcessor):

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return bool(data) and all(
                isinstance(item, str) for item in data
            )
        return False

    def ingest(self, data: typing.Union[str, list[str]]) -> None:
        if not self.validate(data):
            raise TypeError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self._storage.append(item)
                self._rank += 1
                self._total += 1
        else:
            self._storage.append(data)
            self._rank += 1
            self._total += 1


class LogProcessor(DataProcessor):

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            return all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in data.items()
            )
        if isinstance(data, list):
            return bool(data) and all(
                isinstance(item, dict) and all(
                    isinstance(k, str) and isinstance(v, str)
                    for k, v in item.items()
                )
                for item in data
            )
        return False

    def ingest(
        self,
        data: typing.Union[dict[str, str], list[dict[str, str]]]
    ) -> None:
        if not self.validate(data):
            raise TypeError("Improper log data")
        if isinstance(data, list):
            for item in data:
                entry: str = (
                    f"{item['log_level']}: {item['log_message']}"
                )
                self._storage.append(entry)
                self._rank += 1
                self._total += 1
        else:
            entry = f"{data['log_level']}: {data['log_message']}"
            self._storage.append(entry)
            self._rank += 1
            self._total += 1


class ExportPlugin(typing.Protocol):

    def process_output(
        self, data: list[tuple[int, str]]
    ) -> None:
        ...


class CSVExportPlugin:

    def process_output(
        self, data: list[tuple[int, str]]
    ) -> None:
        if not data:
            return
        csv_line: str = ','.join(value for _, value in data)
        print("CSV Output:")
        print(csv_line)


class JSONExportPlugin:

    def process_output(
        self, data: list[tuple[int, str]]
    ) -> None:
        if not data:
            return
        pairs: list[str] = [
            f'"item_{rank}": "{value}"' for rank, value in data
        ]
        json_str: str = '{' + ', '.join(pairs) + '}'
        print("JSON Output:")
        print(json_str)


class DataStream:

    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            handled: bool = False
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    handled = True
                    break
            if not handled:
                print(
                    f"DataStream error - Can't process element"
                    f" in stream: {element}"
                )

    def output_pipeline(
        self, nb: int, plugin: ExportPlugin
    ) -> None:
        for proc in self._processors:
            collected: list[tuple[int, str]] = []
            for _ in range(nb):
                if proc.get_remaining() == 0:
                    break
                collected.append(proc.output())
            if collected:
                plugin.process_output(collected)

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            print(
                f"{proc.get_name()}: total {proc.get_total()} items"
                f" processed, remaining {proc.get_remaining()}"
                f" on processor"
            )


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")

    stream: DataStream = DataStream()
    print("\nInitialize Data Stream...")
    stream.print_processors_stats()

    print("\nRegistering Processors")
    num_proc: NumericProcessor = NumericProcessor()
    txt_proc: TextProcessor = TextProcessor()
    log_proc: LogProcessor = LogProcessor()
    stream.register_processor(num_proc)
    stream.register_processor(txt_proc)
    stream.register_processor(log_proc)

    batch1: list[typing.Any] = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING',
             'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO',
             'log_message': 'User wil is connected'}
        ],
        42,
        ['Hi', 'five']
    ]
    print(f"\nSend first batch of data on stream: {batch1}")
    stream.process_stream(batch1)
    stream.print_processors_stats()

    csv_plugin: CSVExportPlugin = CSVExportPlugin()
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, csv_plugin)
    stream.print_processors_stats()

    batch2: list[typing.Any] = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {'log_level': 'ERROR',
             'log_message': '500 server crash'},
            {'log_level': 'NOTICE',
             'log_message': 'Certificate expires in 10 days'}
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]
    print(f"\nSend another batch of data: {batch2}")
    stream.process_stream(batch2)
    stream.print_processors_stats()

    json_plugin: JSONExportPlugin = JSONExportPlugin()
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, json_plugin)
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
