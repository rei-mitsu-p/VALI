export const MESSAGE = {
  REQUIRED: "{0} is Required",

  format: (template: string, ...params: string[]): string => {
    return template.replace(
      /\{(\w+)\}/g,
      (_: string, index: string) => params[Number(index)] ?? ""
    );
  },
};
