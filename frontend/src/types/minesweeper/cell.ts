export class Cell {
  constructor(
    public x: number,
    public y: number,
    public hasBomb = false,
    public isOpened = false,
    public contents = ""
  ) {}
}
