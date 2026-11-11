import { marked } from 'marked';

/** Markdown from our own data files (trusted, so no sanitizing). */
export const markdown = (text: string | null | undefined) => (text ? (marked.parse(text, { async: false }) as string) : '');
