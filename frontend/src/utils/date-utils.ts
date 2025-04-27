const getCurrentHHmm = (): string => {
  const now = new Date();
  return [now.getHours(), now.getMinutes()]
    .map((s) => String(s).padStart(2, "0"))
    .join(":");
};

const secondsToHhmmss = (seconds: number): string => {
  return [
    Math.floor(seconds / 3600),
    Math.floor((seconds % 3600) / 60),
    seconds % 60,
  ]
    .map((s) => String(s).padStart(2, "0"))
    .join(":");
};

export { getCurrentHHmm, secondsToHhmmss };
