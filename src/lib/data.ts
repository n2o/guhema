// Product data. The JSON files in src/data are the source of truth.
import type { Translated } from './i18n';
import bandsawIndicatorsJson from '../data/bandsawindicators.json';
import circularIndicatorsJson from '../data/circularindicators.json';
import clampingsJson from '../data/clampings.json';
import holesawDiametersJson from '../data/holesawdiameters.json';
import holesawsJson from '../data/holesaws.json';
import indicatorsJson from '../data/indicators.json';
import productgroupsJson from '../data/productgroups.json';
import sawbladesJson from '../data/sawblades.json';

export interface ProductGroup {
  id: number;
  name: Translated;
  description: Translated;
  slug: string;
  image: string | null;
  public: boolean;
}

export interface Clamping {
  id: number;
  name: string;
  slug: string;
  image: Translated;
}

/** Kennziffer of machine/jig/sabre/hack saw blades; tooth-count columns are booleans. */
export interface Indicator {
  id: number;
  value: string;
  width: number;
  strength: number;
  length: number;
  diameter: string;
  [toothColumn: string]: string | number | boolean;
}

export type BladeKind = 'sawblade' | 'sablesawblade' | 'hacksawblade' | 'bandsawblade' | 'jigsawblade' | 'circularsawblade';

/** All SawBlade subclasses flattened; fields of other kinds are simply absent. */
export interface SawBlade {
  kind: BladeKind;
  id: number;
  quality: string;
  type: string;
  name: Translated;
  description: Translated;
  group: number | null;
  clamping: number | null;
  slug: string | null;
  image: Translated;
  indicators: number[];
  // sablesawblade / hacksawblade
  toothing?: Translated;
  cutting_metal?: string | null;
  cutting_wood?: string | null;
  cutting_minerals?: Translated;
  accessory?: boolean;
  subcategory?: Translated;
  // bandsawblade
  bandsaw_indicators?: number[];
  type_description?: Translated;
  type2?: string;
  type2_description?: Translated;
  image2?: Translated;
  heading?: Translated;
  cols?: string;
  // jigsawblade
  tooth_separation?: number;
  length?: number;
  // circularsawblade
  circular_indicators?: number[];
}

export interface HoleSaw {
  id: number;
  ordernr: string;
  image: string | null;
  description: Translated;
  category: Translated;
  mounting: Translated;
  saw_length: string;
  pilot_drill_length: string;
  quality: string;
  toothing: string;
}

export interface HoleSawDiameter {
  id: number;
  diameter: number;
  blades: number[];
  advice: boolean;
  niro: number | null;
  iron: number | null;
  steel: number | null;
  non_ferrous_metals: number | null;
  alu: number | null;
}

export interface BandSawBladeIndicator {
  id: number;
  value: string;
  width: number;
  strength: number;
  [toothColumn: string]: string | number;
}

export interface CircularSawBladeIndicator {
  id: number;
  value: string;
  diameter: number;
  strength: number;
  bore: number;
  NL: string | null;
  [column: string]: string | number | null;
}

export const productGroups = productgroupsJson as ProductGroup[];
export const clampings = clampingsJson as Clamping[];
export const indicators = indicatorsJson as Indicator[];
export const sawBlades = sawbladesJson as unknown as SawBlade[];
export const holeSaws = holesawsJson as HoleSaw[];
export const holeSawDiameters = holesawDiametersJson as HoleSawDiameter[];
export const bandSawIndicators = bandsawIndicatorsJson as BandSawBladeIndicator[];
export const circularIndicators = circularIndicatorsJson as CircularSawBladeIndicator[];

const byId = <T extends { id: number }>(rows: T[]) => new Map(rows.map((r) => [r.id, r]));
const pick = <T extends { id: number }>(map: Map<number, T>, ids: number[] = []) => ids.map((id) => map.get(id)!);

const clampingsById = byId(clampings);
const indicatorsById = byId(indicators);
const holeSawsById = byId(holeSaws);
const bandSawIndicatorsById = byId(bandSawIndicators);
const circularIndicatorsById = byId(circularIndicators);

/** Lists are in id order (the original database order). */
export const groupBySlug = (slug: string) => productGroups.find((g) => g.slug === slug);
export const publicGroups = () => productGroups.filter((g) => g.public);
export const bladesOfGroup = (group: ProductGroup) => sawBlades.filter((b) => b.group === group.id);
export const clampingOf = (blade: SawBlade) => (blade.clamping == null ? undefined : clampingsById.get(blade.clamping));
/** M2M in id order; sort at the call site where the template had order_by. */
export const indicatorsOf = (blade: SawBlade) => pick(indicatorsById, blade.indicators);
export const bandSawIndicatorsOf = (blade: SawBlade) => pick(bandSawIndicatorsById, blade.bandsaw_indicators);
export const circularIndicatorsOf = (blade: SawBlade) => pick(circularIndicatorsById, blade.circular_indicators);
export const holeSawsOf = (d: HoleSawDiameter) => pick(holeSawsById, d.blades);

/** Stable sort by a numeric key. */
export const sortBy = <T>(rows: T[], key: (r: T) => number) => [...rows].sort((a, b) => key(a) - key(b));

/** True where the key differs from the previous row's (and for the first row): show a group heading there. */
export const changed = <T>(keys: T[]) => keys.map((key, i) => i === 0 || key !== keys[i - 1]);

/** URL path segment of a detail page: band saw blades by id, others by type. */
const detailItem = (group: ProductGroup, blade: SawBlade) => (group.slug === 'metallsagebander' ? String(blade.id) : blade.type);
export const detailPath = (group: ProductGroup, blade: SawBlade) => `/produkte/${group.slug}/${detailItem(group, blade)}/`;

/** Detail pages of a group (rendered only for groups with a Details.astro); the first blade wins per item. */
export function detailItems(group: ProductGroup): { item: string; blade: SawBlade }[] {
  const items = new Map<string, SawBlade>();
  for (const blade of bladesOfGroup(group)) {
    const item = detailItem(group, blade);
    if (!items.has(item)) items.set(item, blade);
  }
  return [...items].map(([item, blade]) => ({ item, blade }));
}
